"""
solution AdventOfCode 2019 day 9 part 1.

https://adventofcode.com/2019/day/9

author: pca

"""

from general.general import read_file
from general.general import get_location_input_files
from app.int_machine import IntMachine


def main(args=None):

    program_code = read_file(get_location_input_files(), 'input_day9.txt')[0]

    m = IntMachine(program_code, [1])
    m.run()

    print(f"Finished, output is {m.output}")


if __name__ == "__main__":
    main()
