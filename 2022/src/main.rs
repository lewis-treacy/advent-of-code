use crate::solutions::exec_day;
use std::env;

mod solutions;
mod solver;

fn main() {
    let day = env::args().nth(1).unwrap().parse().unwrap();
    exec_day(day)
}
