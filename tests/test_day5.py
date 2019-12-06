import pytest
import app.day5_1


class TestDay5:

    def test_decode_1(self):
        m = app.day5_1.IntMachine("", [])

        opcode, param_modes = m.decode_instruction(1002)

        assert (opcode, param_modes) == (2, (0, 1, 0))

    def test_decode_2(self):
        m = app.day5_1.IntMachine("", [])

        opcode, param_modes = m.decode_instruction(11103)

        assert (opcode, param_modes) == (3, (1, 1, 1))

    def test_get_value(self):
        m = app.day5_1.IntMachine("1101,2,-1,4,0", [])

        assert m.get_value(1, 1) == 2
        assert m.get_value(1, 0) == -1

    def test_multiply(self):
        m = app.day5_1.IntMachine("1002,4,3,4,33", [])
        m.execute_instruction()

        assert m.memory[4] == 99

    def test_output(self):
        m = app.day5_1.IntMachine("4,3,4,5,33", [])
        m.execute_instruction()

        assert m.output == [5]

    def test_input(self):
        m = app.day5_1.IntMachine("3,2,4,5,33", [55])
        m.execute_instruction()

        assert m.memory[2] == 55

