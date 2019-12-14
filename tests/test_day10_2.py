import pytest
import app.day10_2
import math

class TestDay10_2:

    def test_angle(self):
        assert app.day10_2.calc_angle((0, 0), (0, 1)) == math.pi
        assert app.day10_2.calc_angle((0, 0), (-1, 0)) / math.pi == 1.5
        assert app.day10_2.calc_angle((0, 0), (0, -1)) == 0
        assert app.day10_2.calc_angle((0, 0), (1, 0)) / math.pi == 0.5

    def test_example_1(self):
        asteroids_input = [
            ".#..#",
            ".....",
            "#####",
            "....#",
            "...##"]

        asteroids = app.day10_2.get_positions(asteroids_input)

        max_visible, _, _ = app.day10_2.find_max_visible(asteroids)

        assert max_visible == 8

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

        asteroids = app.day10_2.get_positions(asteroids_input)
        max_visible, _, _ = app.day10_2.find_max_visible(asteroids)

        assert max_visible == 33

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

        asteroids = app.day10_2.get_positions(asteroids_input)

        max_visible, _, _ = app.day10_2.find_max_visible(asteroids)

        assert max_visible == 35

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

        asteroids = app.day10_2.get_positions(asteroids_input)

        max_visible, _, _ = app.day10_2.find_max_visible(asteroids)

        assert max_visible == 41


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

        asteroids = app.day10_2.get_positions(asteroids_input)

        max_visible, _, _ = app.day10_2.find_max_visible(asteroids)

        assert max_visible == 210


    def test_example_6(self):
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

        asteroids = app.day10_2.get_positions(asteroids_input)

        max_visible, max_lines, max_asteroid = app.day10_2.find_max_visible(asteroids)

        vaporize = app.day10_2.order_vaporize(max_lines)

        assert vaporize[199][1] == 8
        assert vaporize[199][2] == 2

