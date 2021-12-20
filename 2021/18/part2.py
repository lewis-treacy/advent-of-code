#!/usr/bin/env python3

import json
from copy import deepcopy

class Number:
    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent

    @classmethod
    def from_list(cls, list, parent=None):
        num = Number(parent = parent)
        num.left = list[0] if isinstance(list[0], int) else Number.from_list(list[0], num)
        num.right = list[1] if isinstance(list[1], int) else Number.from_list(list[1], num)
        return num

    def __add__(self, other):
        left = deepcopy(self)
        right = deepcopy(other)
        num = Number(left, right)
        left.parent = num
        right.parent = num
        num.expload()
        while num.split():
            num.expload()
        return num

    def expload(self, depth=0):
        if depth >= 4:
            self.parent.add_left(self.left, self, True)
            self.parent.add_right(self.right, self, True)
            return True

        if isinstance(self.left, Number) and self.left.expload(depth+1):
            self.left = 0

        if isinstance(self.right, Number) and self.right.expload(depth+1):
            self.right = 0

        return False

    def add_left(self, val, origin, right=False):
        if isinstance(self.left, int):
            self.left += val
            return

        if self.left == origin:
            if self.parent == None:
                return
            self.parent.add_left(val, self, True)
            return

        if right:
            self.left.add_right(val, origin)
            return

        self.left.add_left(val, origin, right)

    def add_right(self, val, origin, left=False):
        if isinstance(self.right, int):
            self.right += val
            return

        if self.right == origin:
            if self.parent == None:
                return
            self.parent.add_right(val, self, True)
            return

        if left:
            self.right.add_left(val, origin)
            return

        self.right.add_right(val, origin, left)

    def split(self):
        #print(f"Split {self}")
        if isinstance(self.left, int):
            if self.left >= 10:
                self.left = Number.do_split(self.left, self)
                return True
        else:
            if self.left.split():
                return True

        if isinstance(self.right, int):
            if self.right >= 10:
                self.right = Number.do_split(self.right, self)
                return True
        else:
            if self.right.split():
                return True

        return False

    @classmethod
    def do_split(cls, num, parent):
        left = num // 2
        right = num - left
        new_num = Number(left, right, parent)
        return new_num

    def magnitude(self):
        left = self.left if isinstance(self.left, int) else self.left.magnitude()
        right = self.right if isinstance(self.right, int) else self.right.magnitude()
        return left * 3 + right * 2

    def __str__(self):
        return f"[{self.left},{self.right}]"

    def __repr__(self):
        return f"[{self.left},{self.right}]"

with open("input.txt", "r") as f:
    numbers = [Number.from_list(json.loads(l)) for l in f]

res = max((a + b).magnitude() for a in numbers for b in numbers if a != b)
print(res)
