"""
solution adventofcode day 7 part 2.

https://adventofcode.com/2019/day/7#part2

author: pca
"""

import argparse
from pathlib import Path
from general.general import read_file
from general.general import get_location_input_files
from app.int_machine import IntMachine
import itertools


def all_phase_settings():
    settings = [5, 6, 7, 8, 9]
    yield from itertools.permutations(settings, len(settings))


def create_machines(phase_setting, program):
    result = list()

    for phase in phase_setting:
        m = IntMachine(program, [phase])
        m.pause_output = True
        result.append(m)

    return result


def run_all_machines(machines):
    machine_input = 0

    for machine in itertools.cycle(machines):
        print(f"Running machine {machine}")

        machine.input.append(machine_input)
        machine.run()
        if machine.halted:
            break

        machine_input = machine.read_next_output()


def main(args=None):
    program = read_file(get_location_input_files(), 'input_day7.txt')[0]

    max_signal = 0

    for phase in all_phase_settings():
        m = create_machines(phase, program)
        run_all_machines(m)
        cur_signal = m[4].last_output
        if cur_signal > max_signal:
            max_signal = cur_signal

    print(f"The highest signal is: {max_signal}")


if __name__ == "__main__":

    main()
