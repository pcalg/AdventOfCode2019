"""

solution adventofcode day1 part 2

https://adventofcode.com/2019/day/1#part2

author: pca
"""

import argparse
from pathlib import Path
from general.general import read_file_int


def fuel_requirement(module_mass):
    """
    Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
    take its mass, divide by three, round down, and subtract 2. Repeat this for the weight of the fuel until the added
    weight is 0.

    :param module_mass:
    :return: fuel_requirement
    """
    total = 0
    current_mass = module_mass

    while (current_mass // 3 - 2) > 0:
        current_mass = current_mass // 3 - 2
        total += current_mass

    return total


def main(args):
    print(args.location)

    puzzle_input = read_file_int(args.location, 'input_day1.txt')

    fuel_requirements = [fuel_requirement(mass) for mass in puzzle_input]

    print(f"The answer is: {sum(fuel_requirements)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='puzzle.')
    parser.add_argument("--location",
                        type=Path,
                        required=True,
                        help="Location puzzles")
    args = parser.parse_args()

    main(args)
