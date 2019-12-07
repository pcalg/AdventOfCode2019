import pytest
import app.day6_1


@pytest.fixture
def orbit_map():
    orbit_map = ["COM)B",
                 "B)C",
                 "C)D",
                 "D)E",
                 "E)F",
                 "B)G",
                 "G)H",
                 "D)I",
                 "E)J",
                 "J)K",
                 "K)L"]
    return [orbit.split(')') for orbit in orbit_map]


class TestDay6:

    def test_total_path(self, orbit_map):
        assert app.day6_1.path_total(orbit_map) == 42
