import pytest
import app.day6_2


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
                 "K)L",
                 "K)YOU",
                 "I)SAN"]
    return [orbit.split(')') for orbit in orbit_map]


class TestDay6_2:

    def test_orbital_transfers(self, orbit_map):
        assert app.day6_2.orbital_transfers(orbit_map, 'YOU', 'SAN') == 4
