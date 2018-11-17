import unittest
from app.find_path import BFSMaze


class TestBFSMaze(unittest.TestCase):

    def test_path_to_right(self):
        maze = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ]

        start = (1, 1,)
        end = (1, 2,)

        path = BFSMaze(maze=maze, start=start,end=end).search()
        expected_path = [(1, 1,), (1,2,)]

        self.assertEqual(path, expected_path)

    def test_no_path(self):
        maze = [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ]

        start = (1, 1,)
        end = (2, 2,)

        path = BFSMaze(maze=maze, start=start, end=end).search()

        self.assertEqual(path, None)


if __name__ == '__main__':
    unittest.main()

