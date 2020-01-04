from app.day16_2 import solve


class TestDay16_2:

    def test_example_2(self):
        assert solve("03036732577212944063491565474664") == "84462026"

    def test_example_2(self):
        assert solve("02935109699940807407585447034323") == "78725270"

    def test_example_3(self):
        assert solve("03081770884921959731165446850517") == "53553731"