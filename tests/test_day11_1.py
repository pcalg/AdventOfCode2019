import pytest
from collections import defaultdict
from app.day11_1 import Robot

class TestDay11_1:

    def test_movement(self):
        r = Robot("", defaultdict(int))
        r.move()
        assert r.position == (-1, 0)
        r.move()
        assert r.position == (-2, 0)
        r.turn(0)
        r.move()
        assert r.position == (-2, -1)
        r.turn(1)
        r.move()
        assert r.position == (-3, -1)
