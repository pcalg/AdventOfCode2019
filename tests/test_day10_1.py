import pytest
import app.day10_1


class TestDay10_1:

    def test_example_1(self):
        asteroids_input = [
            ".#..#",
            ".....",
            "#####",
            "....#",
            "...##"]

        asteroids = app.day10_1.get_positions(asteroids_input)

        assert app.day10_1.find_max_visible(asteroids) == 8

    def test_example_2(self):
        asteroids_input = [
            "......#.#.",
            "#..#.#....",
            "..#######.",
            ".#.#.###..",
            ".#..#.....",
            "..#....#.#",
            "#..#....#.",
            ".##.#..###",
            "##...#..#.",
            ".#....####"]

        asteroids = app.day10_1.get_positions(asteroids_input)

        assert app.day10_1.find_max_visible(asteroids) == 33

    def test_example_3(self):
        asteroids_input = [
            "# .#...#.#.",
            ".###....#.",
            ".#....#...",
            "##.#.#.#.#",
            "....#.#.#.",
            ".##..###.#",
            "..#...##..",
            "..##....##",
            "......#...",
            ".####.###."]

        asteroids = app.day10_1.get_positions(asteroids_input)

        assert app.day10_1.find_max_visible(asteroids) == 35

    def test_example_4(self):
        asteroids_input = [
            ".#..#..###",
            "####.###.#",
            "....###.#.",
            "..###.##.#",
            "##.##.#.#.",
            "....###..#",
            "..#.#..#.#",
            "#..#.#.###",
            ".##...##.#",
            ".....#.#.."]

        asteroids = app.day10_1.get_positions(asteroids_input)

        assert app.day10_1.find_max_visible(asteroids) == 41

    def test_example_5(self):
        asteroids_input = [
            ".#..##.###...#######",
            "##.############..##.",
            ".#.######.########.#",
            ".###.#######.####.#.",
            "#####.##.#.##.###.##",
            "..#####..#.#########",
            "####################",
            "#.####....###.#.#.##",
            "##.#################",
            "#####.##.###..####..",
            "..######..##.#######",
            "####.##.####...##..#",
            ".#####..#.######.###",
            "##...#.##########...",
            "#.##########.#######",
            ".####.#.###.###.#.##",
            "....##.##.###..#####",
            ".#.#.###########.###",
            "#.#.#.#####.####.###",
            "###.##.####.##.#..##"]

        asteroids = app.day10_1.get_positions(asteroids_input)

        assert app.day10_1.find_max_visible(asteroids) == 210




