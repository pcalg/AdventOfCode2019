"""
solution AdventOfCode 2019 day 15 part 1.

https://adventofcode.com/2019/day/15.

author: pca

"""

from general.general import read_file
from general.general import get_location_input_files
from collections import defaultdict
from app.int_machine import IntMachine
import functools


def input_generator(grid, m: IntMachine):
    grid[(1, 1)] = '#'

    if len(m.output) > 1:
        print(m.read_next_output())
    return 1


def main(args=None):

    grid = defaultdict(str)

    program_code = read_file(get_location_input_files(), 'input_day15.txt')[0]
    m = IntMachine(program_code, [])
    m.input_retriever = functools.partial(input_generator, grid)
    m.max_steps = 550000
    m.run()


if __name__ == "__main__":
    main()
