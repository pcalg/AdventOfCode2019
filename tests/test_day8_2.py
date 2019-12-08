import pytest
import app.day8_2


class TestDay8_2:

    def test_layers(self):
        layers = list(app.day8_2.make_layers((3, 2), "123456789012"))

        assert len(layers) == 2
        assert layers[0] == '123456'
        assert layers[1] == '789012'

    def test_collect_image_data(self):
        dimensions = (2, 2)
        layers = list(app.day8_2.make_layers(dimensions, "0222112222120000"))

        image_data = app.day8_2.collect_image_data(dimensions, layers)

        assert image_data[(0, 0)] == (0, 0, 0)
        assert image_data[(1, 0)] == (255, 255, 255)
        assert image_data[(0, 1)] == (255, 255, 255)
        assert image_data[(1, 1)] == (0, 0, 0)


