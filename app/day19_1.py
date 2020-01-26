"""
solution AdventOfCode 2019 day 19 part 1.

https://adventofcode.com/2019/day/19.

author: pca

"""

from general.general import read_file
from general.general import get_location_input_files
from general.general import measure
from app.int_machine import IntMachine
from collections import defaultdict
from general.visualize import visualize_grid

def main(args=None):
    program_code = read_file(get_location_input_files(), 'input_day19.txt')[0]

    grid = defaultdict(str)

    cnt = 0

    for x in range(50):
        for y in range(50):
            m = IntMachine(program_code, [x, y])
            m.silent = True
            m.run()
            if m.output == [1]:
                grid[(y, x)] = '#'
                cnt += 1
            else:
                grid[(y, x)] = '.'


    img = visualize_grid(grid, (50, 50), colors={'#': 'blue', '.': 'white'})
    img.show()

    print(m.output)
    print(f"result: {cnt}")



if __name__ == "__main__":
    main()
