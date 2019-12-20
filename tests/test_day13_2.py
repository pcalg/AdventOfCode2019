import pytest
import app.day13_2


class TestDay13_2:

    def test_instructions(self):

        tiles = app.day13_2.decode_instructions([1, 2, 3, 6, 5, 4])
        assert (1, 2) in tiles
        assert (6, 5) in tiles
        assert tiles[(1, 2)] == 3
        assert tiles[(6, 5)] == 4

    def test_location(self):
        tiles = app.day13_2.decode_instructions([1, 2, 3, 6, 5, 4])

        assert app.day13_2.get_location(tiles, app.day13_2.Tiles.BALL) == (6, 5)
        assert app.day13_2.get_location(tiles, app.day13_2.Tiles.PADDLE) == (1, 2)

    def test_count_tiles(self):
        tiles = app.day13_2.decode_instructions([1, 2, 3, 6, 5, 4, 10, 11, 2, 11, 12, 2, 13, 15, 0])

        assert app.day13_2.cnt_tiles(tiles, app.day13_2.Tiles.BLOCK) == 2
        assert app.day13_2.cnt_tiles(tiles, app.day13_2.Tiles.PADDLE) == 1
        assert app.day13_2.cnt_tiles(tiles, app.day13_2.Tiles.BALL) == 1
        assert app.day13_2.cnt_tiles(tiles, app.day13_2.Tiles.WALL) == 0
