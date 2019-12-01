"""
solution adventofcode day1

https://adventofcode.com/2019/day/1

author: pca
"""

import argparse
from pathlib import Path
from general.general import read_file_int


def fuel_requirement(module_mass):
    """
    Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
    take its mass, divide by three, round down, and subtract 2.

    :param module_mass:
    :return: fuel_requirement
    """
    return module_mass // 3 - 2


def main(args):
    print(args.location)

    puzzle_input = read_file_int(args.location, 'input_day1.txt')

    fuel_requirements = [fuel_requirement(mass) for mass in puzzle_input]

    print(sum(fuel_requirements))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='puzzle.')
    parser.add_argument("--location",
                        type=Path,
                        required=True,
                        help="Location puzzles")
    args = parser.parse_args()

    main(args)
