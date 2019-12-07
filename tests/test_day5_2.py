import pytest
import app.day5_2


class TestDay5_2:

    def test_decode_1(self):
        opcode, param_modes = app.day5_2.IntMachine.decode_instruction(1002)

        assert (opcode, param_modes) == (2, (0, 1, 0))

    def test_decode_2(self):
        opcode, param_modes = app.day5_2.IntMachine.decode_instruction(11103)

        assert (opcode, param_modes) == (3, (1, 1, 1))

    def test_get_value(self):
        m = app.day5_2.IntMachine("1101,2,-1,4,0", [])

        assert m.get_value(1, 1) == 2
        assert m.get_value(1, 0) == -1

    def test_multiply(self):
        m = app.day5_2.IntMachine("1002,4,3,4,33", [])
        m.execute_instruction()

        assert m.memory[4] == 99

    def test_output(self):
        m = app.day5_2.IntMachine("4,3,4,5,33", [])
        m.execute_instruction()

        assert m.output == [5]

    def test_input(self):
        m = app.day5_2.IntMachine("3,2,4,5,33", [55])
        m.execute_instruction()

        assert m.memory[2] == 55

    def test_example_1(self):
        m = app.day5_2.IntMachine("3,9,8,9,10,9,4,9,99,-1,8", [8])
        m.run()

        assert m.output == [1]

    def test_example_2(self):
        m = app.day5_2.IntMachine("3,9,7,9,10,9,4,9,99,-1,8", [8])
        m.run()

        assert m.output == [0]

    def test_example_3(self):
        m = app.day5_2.IntMachine("3,3,1108,-1,8,3,4,3,99", [8])
        m.run()

        assert m.output == [1]

    def test_example_4(self):
        m = app.day5_2.IntMachine("3,3,1107,-1,8,3,4,3,99", [8])
        m.run()

        assert m.output == [0]
