"""
solution AdventOfCode 2019 day 14 part 1.

https://adventofcode.com/2019/day/14.

author: pca

"""

from general.general import read_file
from general.general import get_location_input_files


def round_up(n, d):
    result = n // d
    if n % d > 0:
        result += 1
    return result


def main(args=None):

    reactions = read_file(get_location_input_files(), 'input_day14.txt')



if __name__ == "__main__":
    main()
