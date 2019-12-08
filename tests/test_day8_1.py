import pytest
import app.day8_1


class TestDay8:

    def test_layers(self):
        layers = list(app.day8_1.make_layers((3, 2), "123456789012"))

        assert len(layers) == 2
        assert layers[0] == '123456'
        assert layers[1] == '789012'



