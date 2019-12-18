import pytest
import app.day13_1


class TestDay13_1:

    def test_instructions(self):

        tiles = app.day13_1.decode_instructions([1, 2, 3, 6, 5, 4])
        assert (1, 2) in tiles
        assert (6, 5) in tiles
        assert tiles[(1, 2)] == 3
        assert tiles[(6, 5)] == 4
