use std::io::Read;
use std::str::FromStr;

use crate::solver::{ReadExt, Solver};

pub struct Problem;

impl Solver for Problem {
    type Input = Vec<Round>;
    type Output1 = u32;
    type Output2 = u32;

    fn parse_input<R: Read>(&self, r: R) -> Self::Input {
        r.split_lines()
    }

    fn solve_first(&self, input: &Self::Input) -> Self::Output1 {
        input.iter().map(|r| r.score1()).sum()
    }

    fn solve_second(&self, input: &Self::Input) -> Self::Output2 {
        input.iter().map(|r| r.score2()).sum()
    }
}

#[derive(Eq, PartialEq, Clone, Copy)]
pub enum Move {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

impl Move {
    fn res(&self, other: &Self) -> Outcome {
        match (self, other) {
            (Move::Rock, Move::Paper) => Outcome::Lose,
            (Move::Rock, Move::Scissors) => Outcome::Win,
            (Move::Paper, Move::Rock) => Outcome::Win,
            (Move::Paper, Move::Scissors) => Outcome::Lose,
            (Move::Scissors, Move::Rock) => Outcome::Lose,
            (Move::Scissors, Move::Paper) => Outcome::Win,
            _ => Outcome::Draw,
        }
    }
}

impl FromStr for Move {
    type Err = &'static str;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "A" => Ok(Move::Rock),
            "B" => Ok(Move::Paper),
            "C" => Ok(Move::Scissors),
            _ => Err("Invalid character"),
        }
    }
}

#[derive(Clone, Copy)]
pub enum Outcome {
    Win = 6,
    Draw = 3,
    Lose = 0,
}

impl FromStr for Outcome {
    type Err = &'static str;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "X" => Ok(Outcome::Lose),
            "Y" => Ok(Outcome::Draw),
            "Z" => Ok(Outcome::Win),
            _ => Err("Invalid character"),
        }
    }
}

impl Outcome {
    fn to_move(&self) -> Move {
        match *self {
            Outcome::Lose => Move::Rock,
            Outcome::Draw => Move::Paper,
            Outcome::Win => Move::Scissors,
        }
    }
}

pub struct Round {
    opponent: Move,
    player: Outcome,
}

impl FromStr for Round {
    type Err = &'static str;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut itr = s.split_whitespace();
        Ok(Round {
            opponent: itr.next().ok_or("missing move")?.parse()?,
            player: itr.next().ok_or("missing move")?.parse()?,
        })
    }
}

impl Round {
    fn score1(&self) -> u32 {
        self.player.to_move() as u32 + self.player.to_move().res(&self.opponent) as u32
    }

    fn score2(&self) -> u32 {
        self.player as u32
            + match (self.opponent, self.player) {
                (Move::Rock, Outcome::Win) => Move::Paper,
                (Move::Rock, Outcome::Lose) => Move::Scissors,
                (Move::Paper, Outcome::Win) => Move::Scissors,
                (Move::Paper, Outcome::Lose) => Move::Rock,
                (Move::Scissors, Outcome::Win) => Move::Rock,
                (Move::Scissors, Outcome::Lose) => Move::Paper,
                (m, Outcome::Draw) => m,
            } as u32
    }
}
