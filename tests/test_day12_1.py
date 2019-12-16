import pytest
from collections import defaultdict
import app.day12_1


class TestDay12_1:

    def test_delta(self):
        assert app.day12_1.calc_delta(1, 5) == 1
        assert app.day12_1.calc_delta(4, 2) == -1
        assert app.day12_1.calc_delta(10, 10) == 0

    def test_new_velocity(self):
        assert app.day12_1.new_velocity((1, 1, 1), (3, 4, 5), (0, 2, 0), (0, 0, -1)) == ((1, 3, 1), (-1, -1, -2))
        assert app.day12_1.new_velocity((1, 1, 1), (1, 4, 5), (0, 2, 0), (0, 0, -1)) == ((0, 3, 1), (0, -1, -2))

    def test_example1(self):
        moon_locations = ["<x=-1, y=0, z=2>",
                          "<x=2, y=-10, z=-7>",
                          "<x=4, y=-8, z=8>",
                          "<x=3, y=5, z=-1>"]

        all_coords = [app.day12_1.convert_coord(location) for location in moon_locations]

        moons = [app.day12_1.Moon(coords) for coords in all_coords]

        s = app.day12_1.Simulation(moons)

        for _ in range(10):
            s.simulate()

        assert s.energy() == 179

    def test_example2(self):
        moon_locations = ["<x=-8, y=-10, z=0>",
                          "<x=5, y=5, z=10>",
                          "<x=2, y=-7, z=3>",
                          "<x=9, y=-8, z=-3>"]

        all_coords = [app.day12_1.convert_coord(location) for location in moon_locations]

        moons = [app.day12_1.Moon(coords) for coords in all_coords]

        s = app.day12_1.Simulation(moons)

        for _ in range(100):
            s.simulate()

        assert s.energy() == 1940
