import pytest
import app.int_machine


class TestIntMachine:

    def test_decode_1(self):
        opcode, param_modes = app.int_machine.IntMachine.decode_instruction(1002)

        assert (opcode, param_modes) == (2, (0, 1, 0))

    def test_decode_2(self):
        opcode, param_modes = app.int_machine.IntMachine.decode_instruction(11103)

        assert (opcode, param_modes) == (3, (1, 1, 1))

    def test_get_value(self):
        m = app.int_machine.IntMachine("1101,2,-1,4,0", [])

        assert m.get_value(1, 1) == 2
        assert m.get_value(1, 0) == -1

    def test_multiply(self):
        m = app.int_machine.IntMachine("1002,4,3,4,33", [])
        m.execute_instruction()

        assert m.memory[4] == 99

    def test_output(self):
        m = app.int_machine.IntMachine("4,3,4,5,33", [])
        m.execute_instruction()

        assert m.output == [5]

    def test_input(self):
        m = app.int_machine.IntMachine("3,2,4,5,33", [55])
        m.execute_instruction()

        assert m.memory[2] == 55

    def test_example_1(self):
        m = app.int_machine.IntMachine("3,9,8,9,10,9,4,9,99,-1,8", [8])
        m.run()

        assert m.output == [1]

    def test_example_2(self):
        m = app.int_machine.IntMachine("3,9,7,9,10,9,4,9,99,-1,8", [8])
        m.run()

        assert m.output == [0]

    def test_example_3(self):
        m = app.int_machine.IntMachine("3,3,1108,-1,8,3,4,3,99", [8])
        m.run()

        assert m.output == [1]

    def test_example_4(self):
        m = app.int_machine.IntMachine("3,3,1107,-1,8,3,4,3,99", [8])
        m.run()

        assert m.output == [0]


    def test_example_9_1(self):
        m = app.int_machine.IntMachine("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99", [])
        m.run()

        assert m.output == [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]

    def test_example_9_2(self):
        m = app.int_machine.IntMachine("1102, 34915192, 34915192, 7, 4, 7, 99, 0", [])
        m.run()

        # 1 output, number of len 16
        assert len(m.output) == 1
        assert len(str(m.output[0])) == 16

    def test_example_9_3(self):
        m = app.int_machine.IntMachine("104,1125899906842624,99", [])
        m.run()

        # 1 output, otuput is the mdidle number
        assert len(m.output) == 1
        assert m.output[0] == 1125899906842624


