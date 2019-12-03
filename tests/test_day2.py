import pytest
import app.day2_1


class TestDay2:
    def test_program1(self):
        program = '1,0,0,0,99'

        state = app.day2_1.create_program_state(program)
        app.day2_1.run_intcode(state)

        assert state[0] == 2

    def test_program2(self):
        program = '2,3,0,3,99'

        state = app.day2_1.create_program_state(program)
        app.day2_1.run_intcode(state)

        assert state[3] == 6

    def test_program3(self):
        program = '2,4,4,5,99,0'

        state = app.day2_1.create_program_state(program)
        app.day2_1.run_intcode(state)

        assert state[5] == 9801

    def test_program4(self):
        program = '1,1,1,4,99,5,6,0,99'

        state = app.day2_1.create_program_state(program)
        app.day2_1.run_intcode(state)

        assert state[0] == 30



