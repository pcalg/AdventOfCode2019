from app.day16_1 import run_all


class TestDay16_1:

    def test_example_1(self):
        signal = [int(ch) for ch in "80871224585914546619083218645595"]

        assert "".join([str(d) for d in run_all(signal)[0:8]]) == "24176176"

    def test_example_2(self):
        signal = [int(ch) for ch in "19617804207202209144916044189917"]

        assert "".join([str(d) for d in run_all(signal)[0:8]]) == "73745418"


    def test_example_3(self):
        signal = [int(ch) for ch in "69317163492948606335995924319873"]

        assert "".join([str(d) for d in run_all(signal)[0:8]]) == "52432133"
