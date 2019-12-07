import pytest
import app.day4_1
import app.day4_2

class TestDay4:
    def test_pw1(self):
        assert app.day4_1.valid_pw('111111')

    def test_pw2(self):
        assert not app.day4_1.valid_pw('223450')

    def test_pw3(self):
        assert not app.day4_1.valid_pw('123789')

class TestDay4_2:
    def test_blocks(self):
        blocks = app.day4_2.equal_digits_blocks("112444")
        assert blocks == [['1', '1'], ['2'], ['4', '4', '4']]

    def test_pw1(self):
        assert app.day4_2.valid_pw('112233')

    def test_pw2(self):
        assert not app.day4_2.valid_pw('123444')

    def test_pw3(self):
        assert app.day4_2.valid_pw('111122')

