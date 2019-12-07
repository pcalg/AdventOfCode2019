"""
solution adventofcode day 6 part 1.

https://adventofcode.com/2019/day/6

author: pca
"""

import argparse
from pathlib import Path
from general.general import read_file
import operator
import networkx as nx


def path_total(orbit_map):
    G = nx.Graph()
    G.add_edges_from(orbit_map)
    path_lengths = nx.single_source_shortest_path_length(G, source='COM')

    return sum(path_lengths.values())


def main(args):
    print(args.location)

    orbit_map = [orbit.split(')') for orbit in read_file(args.location, 'input_day6.txt')]

    total = path_total(orbit_map)

    print(f"Total length is: {total}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='puzzle.')
    parser.add_argument("--location",
                        type=Path,
                        required=True,
                        help="Location puzzles")
    args = parser.parse_args()

    main(args)
