from app.day17_2 import cross2d
from app.day17_2 import len_route
from app.day17_2 import all_sub_lists
from app.day17_2 import possible_register_values
from app.day17_2 import has_possible_route


class TestDay17_2:

    def test_cross2d(self):
        assert cross2d((0, 1), (1, 0)) == -1
        assert cross2d((0, 1), (0, 1)) == 0
        assert cross2d((0, 1), (-1, 0)) == 1
        assert cross2d((1, 0), (0, 1)) == 1
        assert cross2d((1, 0), (0, -1)) == -1
        assert cross2d((-1, 0), (0, 1)) == -1
        assert cross2d((-1, 0), (0, -1)) == 1

    def test_len_route(self):
        assert len_route([]) == 0
        assert len_route([('R', 1)]) == 3
        assert len_route([('R', 1), ('L', 33), ('R', 9)]) == 12

    def test_all_sub_lists(self):
        assert list(all_sub_lists([('R', 1), ('L', 33), ('R', 9)])) == \
               [[('R', 1)],
                [('R', 1), ('L', 33)],
                [('R', 1), ('L', 33), ('R', 9)],
                [('L', 33)],
                [('L', 33), ('R', 9)],
                [('R', 9)]]

    def test_possible_register_values(self):
        possible_values = list(possible_register_values([('R', 1), ('L', 33), ('R', 9)]))
        assert len(possible_values) == 20
        assert ([('R', 1), ('L', 33)], [('L', 33)], [('L', 33), ('R', 9)]) in possible_values

    def test_has_possible_route(self):
        res, actions = has_possible_route([('R', 1), ('L', 33), ('R', 9), ('R', 9)],
                                          [[('R', 9)], [('R', 1), ('L', 33)], []])
        assert res == True
        assert actions == [1, 0, 0]
