import pytest
import app.day7_1


class TestDay7:

    def test_all_phase_settings(self):
        settings = list(app.day7_1.all_phase_settings())
        assert len(settings) == 120
        assert (1, 3, 4, 0, 2) in settings
        assert (1, 4, 2, 3, 0) in settings
        assert (0, 0, 0, 0, 0) not in settings

    def test_program_1(self):
        program = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
        phase = (4, 3, 2, 1, 0)
        m = app.day7_1.create_machines(phase, program)
        app.day7_1.run_all_machines(m)
        assert m[4].output[0] == 43210

    def test_program_2(self):
        program = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
        phase = (0, 1, 2, 3, 4)
        m = app.day7_1.create_machines(phase, program)
        app.day7_1.run_all_machines(m)
        assert m[4].output[0] == 54321

    def test_program_3(self):
        program = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
        phase = (1, 0, 4, 3, 2)
        m = app.day7_1.create_machines(phase, program)
        app.day7_1.run_all_machines(m)
        assert m[4].output[0] == 65210




