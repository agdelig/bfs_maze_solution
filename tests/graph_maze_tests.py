import unittest
from app.graph_maze import GraphMaze


class TestGraphMaze(unittest.TestCase):

    def test_no_child_nodes(self):
        maze = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]

        graph = GraphMaze(maze).nodes

        self.assertEqual(graph, {(1, 1,): []})

    def test_north_south_child(self):
        maze = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

        graph = GraphMaze(maze).nodes

        expected_nodes = {
            (1, 1,): [(1, 2,)],
            (1, 2,): [(1, 1,)]
        }

        self.assertEqual(graph, expected_nodes)

    def test_east_west_child(self):
        maze = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ]

        graph = GraphMaze(maze).nodes

        expected_nodes = {
            (1, 1,): [(2, 1,)],
            (2, 1,): [(1, 1,)]
        }

        self.assertEqual(graph, expected_nodes)

    def test_surrounded_by_children(self):
        maze = [
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1]
        ]

        graph = GraphMaze(maze).nodes

        expected_nodes = {
            (2, 1,): [(2, 2,)],
            (1, 2,): [(2, 2,)],
            (2, 2,): [(2, 1,), (3, 2,), (2, 3,), (1, 2,)],
            (3, 2,): [(2, 2,)],
            (2, 3,): [(2, 2,)]
        }

        self.assertEqual(graph, expected_nodes)


if __name__ == '__main__':
    unittest.main()

