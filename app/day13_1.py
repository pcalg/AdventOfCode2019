"""
solution AdventOfCode 2019 day 13 part 1.

https://adventofcode.com/2019/day/13.

author: pca

"""

from general.general import read_file
from general.general import get_location_input_files
from app.int_machine import IntMachine


def decode_instructions(instructions):
    if len(instructions) % 3 != 0:
        raise ValueError("Expected all instructions to be in pairs of 3 (x, y, tile")

    tiles = dict()

    for idx in range(0, len(instructions), 3):
        x, y, tile = instructions[idx:idx+3]
        tiles[(x, y)] = tile

    return tiles


def main(args=None):

    program_code = read_file(get_location_input_files(), 'input_day13.txt')[0]

    m = IntMachine(program_code, [])

    m.run()

    output_instructions = m.output

    tiles = decode_instructions(output_instructions)

    # count block tiles (2)
    cnt = 0
    for tile in tiles.values():
        if tile == 2:
            cnt += 1

    print(f"Block tiles: {cnt}")


if __name__ == "__main__":
    main()
