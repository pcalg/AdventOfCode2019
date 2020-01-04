"""
solution AdventOfCode 2019 day 17 part 1.

https://adventofcode.com/2019/day/17.

author: pca

"""

from general.general import read_file
from general.general import get_location_input_files
from general.general import measure
from app.int_machine import IntMachine
from collections import defaultdict

def print_grid(ascii_output):
    for ch in ascii_output:
        if ch == '\n':
            print("")
        else:
            print(ch, end="")
    print("")


def to_grid(ascii_output):
    grid = defaultdict(lambda: '.')
    x = 0
    y = 0
    for ch in ascii_output:
        if ch == '\n':
            y += 1
            x = 0
        else:
            grid[(y, x)] = ch
            x += 1

    return grid

def is_intersection(grid, pos):
    y, x = pos
    deltas = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    for dy, dx in deltas:
        if grid[(y + dy, x + dx)] != '#':
            return False
    return True

@measure
def solve(grid):

    alignment_sum = 0

    positions = list(grid.keys())

    for pos in positions:
        if is_intersection(grid, pos):
            y, x = pos
            alignment_sum += (y * x)

    return alignment_sum



def main(args=None):

    program_code = read_file(get_location_input_files(), 'input_day17.txt')[0]

    m = IntMachine(program_code, [])

    m.run()

    # convert output to ascii
    ascii_output = [chr(val) for val in m.output]

    g = to_grid(ascii_output)

    total = solve(g)

    print(f"Alignment sum: {total}")

if __name__ == "__main__":
    main()
