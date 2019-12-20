import pytest
import app.day14_1
from app.day14_1 import parse_quantity
from app.day14_1 import parse_reaction
from app.day14_1 import round_up


class TestDay14_1:
    def test_round_up(self):
        assert round_up(48, 5) == 10
        assert round_up(50, 5) == 10

    def test_parse_quantity(self):

        assert parse_quantity('51 DMLM') == ('DMLM', 51)
        assert parse_quantity(' 8 AB') == ('AB', 8)
        assert parse_quantity(' 91 BAB ') == ('BAB', 91)

    def test_parse_reaction(self):
        reaction = "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ"

        assert parse_reaction(reaction) == (('QDVJ', 9), [('HKGWZ', 12), ('GPVTF', 1), ('PSHF', 8)])

