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


def parse_quantity(quantity):
    q = quantity.strip().split(' ')
    return q[1], int(q[0])

def parse_reaction(reaction):
    r = reaction.split(' => ')

    output_quantity = parse_quantity(r[-1])

    input_quantities = [parse_quantity(q) for q in r[0].split(',')]

    return output_quantity, input_quantities



def main(args=None):

    reaction_codes = read_file(get_location_input_files(), 'input_day14.txt')

    reactions = [parse_reaction(r) for r in reaction_codes]



if __name__ == "__main__":
    main()
