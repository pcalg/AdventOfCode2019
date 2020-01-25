from app.day18_1 import create_grid2d, reachable_graph, solve


class TestDay18_1:

    def test_example_1(self):

        grid_txt = ["#########",
                    "#b.A.@.a#",
                    "#########"]

        grid2d, nodes = create_grid2d(grid_txt)

        distances, neighbours = reachable_graph(grid2d, nodes)

        dist = solve(distances, neighbours)

        assert dist == 8

    def test_example_2(self):

        grid_txt = ["########################",
                    "#f.D.E.e.C.b.A.@.a.B.c.#",
                    "######################.#",
                    "#d.....................#",
                    "########################"]

        grid2d, nodes = create_grid2d(grid_txt)

        distances, neighbours = reachable_graph(grid2d, nodes)

        dist = solve(distances, neighbours)

        assert dist == 86

    def test_example_3(self):

        grid_txt = ["########################",
                    "#...............b.C.D.f#",
                    "#.######################",
                    "#.....@.a.B.c.d.A.e.F.g#",
                    "########################"]

        grid2d, nodes = create_grid2d(grid_txt)

        distances, neighbours = reachable_graph(grid2d, nodes)

        dist = solve(distances, neighbours)

        assert dist == 132

    def test_example_4(self):

        grid_txt = ["#################",
                    "#i.G..c...e..H.p#",
                    "########.########",
                    "#j.A..b...f..D.o#",
                    "########@########",
                    "#k.E..a...g..B.n#",
                    "########.########",
                    "#l.F..d...h..C.m#",
                    "#################"]

        grid2d, nodes = create_grid2d(grid_txt)

        distances, neighbours = reachable_graph(grid2d, nodes)

        dist = solve(distances, neighbours)

        assert dist == 136

    def test_example_5(self):
        grid_txt = ["########################",
                    "#@..............ac.GI.b#",
                    "###d#e#f################",
                    "###A#B#C################",
                    "###g#h#i################",
                    "########################"]

        grid2d, nodes = create_grid2d(grid_txt)

        distances, neighbours = reachable_graph(grid2d, nodes)

        dist = solve(distances, neighbours)

        assert dist == 81
