from app.graph_maze import GraphMaze


class BFSMaze:
    '''
    Class used to find mazew path frm start to end point.
    '''
    def __init__(self, maze, start, end):
        '''
        Constructor
        :param maze: Two dimention array representing maze.
        :param start: Tuple representing start point of (x, y) values.
        :param end: Tuple representing end point of (x, y) values.
        '''
        self._graph = GraphMaze(maze).nodes
        self.start = start
        self.end = end
        self.found = False

    def search(self):
        '''
        Funtion to find path from start to end point.
        If no path is found function returns None.
        This function is a BFS algorithm.
        :return: valid path if found or None
        '''
        node_que = [[self.start]] # A list of all paths to be checked.
        visited_nodes = [] # A list of nodes already checked to avoid checking the same nodes multiple times.
                           # Nodes are represented as tuples of (x, y) values.
        valid_path = [] # List of nodes showing the path from start to end point.

        while len(node_que) > 0:
            path_to_check = node_que.pop()

            node_to_check = path_to_check[-1]
            visited_nodes.append(node_to_check)

            if node_to_check == self.end:
                self.found = True
                node_que = []
                valid_path = path_to_check

            else:
                for n in self._graph.get(node_to_check):
                    p = path_to_check.copy() # Make a copy of the path leading to current node to add to que
                    if n not in visited_nodes:
                        p.append(n)
                        node_que.append(p)

        return valid_path if self.found else None
''''''
