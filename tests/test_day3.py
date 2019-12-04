import pytest
from collections import defaultdict
import app.day3_1
import app.day3_2

class TestDay3:
    def test_path1(self):
        grid = defaultdict(set)
        wires = list()
        wires.append('R75,D30,R83,U83,L12,D49,R71,U7,L72')
        wires.append('U62,R66,U55,R34,D71,R55,D58,R83')

        app.day3_1.add_wires(grid, wires)

        min_dist = min(app.day3_1.distances_crossings(grid))

        assert min_dist == 159

    def test_path2(self):
        grid = defaultdict(set)
        wires = list()
        wires.append('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51')
        wires.append('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')

        app.day3_1.add_wires(grid, wires)

        min_dist = min(app.day3_1.distances_crossings(grid))

        assert min_dist == 135

class TestDay3_2:
    def test_path1(self):

        wires = list()
        wires.append('R75,D30,R83,U83,L12,D49,R71,U7,L72')
        wires.append('U62,R66,U55,R34,D71,R55,D58,R83')

        grid = defaultdict(set)
        routes = list()

        app.day3_2.add_wires(grid, routes, wires)
        crossings = app.day3_2.find_crossings(grid)
        all_steps = app.day3_2.find_steps(routes, crossings)

        assert min(all_steps) == 610

    def test_path2(self):

        wires = list()
        wires.append('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51')
        wires.append('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')

        grid = defaultdict(set)
        routes = list()

        app.day3_2.add_wires(grid, routes, wires)
        crossings = app.day3_2.find_crossings(grid)
        all_steps = app.day3_2.find_steps(routes, crossings)

        assert min(all_steps) == 410

