use crate::solver::Solver;

mod day01;
mod day02;

pub fn exec_day(day: u32) {
    match day {
        1 => day01::Problem {}.solve(day),
        2 => day02::Problem {}.solve(day),

        d => println!("Day {d} hasn't been solved yet :("),
    }
}
