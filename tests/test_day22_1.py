from app.day22_1 import run

class TestDay22_1:

    def test_example_1(self):
        instructions = ["deal with increment 7",
                        "deal into new stack",
                        "deal into new stack"]

        assert list(run(10, instructions)) == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]

    def test_example_2(self):
        instructions = ["cut 6",
                        "deal with increment 7",
                        "deal into new stack"]

        assert list(run(10, instructions)) == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]

    def test_example_3(self):
        instructions = ["deal with increment 7",
                        "deal with increment 9",
                        "cut -2"]

        assert list(run(10, instructions)) == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]

    def test_example_4(self):
        instructions = ["deal into new stack",
                        "cut -2",
                        "deal with increment 7",
                        "cut 8",
                        "cut -4",
                        "deal with increment 7",
                        "cut 3",
                        "deal with increment 9",
                        "deal with increment 3",
                        "cut -1"]

        assert list(run(10, instructions)) == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]
