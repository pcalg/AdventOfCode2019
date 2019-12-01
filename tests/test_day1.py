import pytest
import app.day1_1
import app.day1_2


class Test_Day1:
    @pytest.mark.parametrize("test_input, expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
    def test_fuel_requirement(self, test_input, expected):
        assert app.day1_1.fuel_requirement(test_input) == expected

    @pytest.mark.parametrize("test_input, expected", [(14, 2), (1969, 966), (100756, 50346)])
    def test_fuel_requirement_part2(self, test_input, expected):
        assert app.day1_2.fuel_requirement(test_input) == expected

