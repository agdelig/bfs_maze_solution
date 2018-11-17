class GraphMaze:
    '''
    Class used to convert maze into a graph.
    Produces a dict with key each node re3presented by a tuple of (x, y) values
    and a list of all child nodes reprewsented by a tuple of (x, y) values.
    '''
    def __init__(self, maze):
        '''
        Constructor function.
        :param maze: Two dimention array representing maze.
        '''
        self._maze = maze
        self._nodes = {}

    @property
    def nodes(self):
        if len(self._nodes) is 0:
            self.init_nodes()

        return self._nodes

    def check_neighbours(self, x, y):
        '''
        Function used to find all neighbouring nodes that are path, that are of 0 value.
        :param x: Parent node x value
        :param y: parent node y value
        :return: list of child nodes
        '''
        links = []

        if self._maze[y][x] == 0:
            #North
            if self._maze[y - 1][x] == 0:
                n = (x, y-1,)
                links.append(n)

            #East
            if self._maze[y][x + 1] == 0:
                e = (x+1, y,)
                links.append(e)

            #South
            if self._maze[y + 1][x] == 0:
                s = (x, y+1,)
                links.append(s)

            #West
            if self._maze[y][x - 1] == 0:
                w = (x-1, y,)
                links.append(w)

        return links #if len(links) > 0 else None

    def init_nodes(self):
        '''
        Function itterating through maze nodes to create graph representing maze.
        :return:
        '''
        for i in range(1, len(self._maze) - 1):
            for j in range(1, len(self._maze[i]) - 1):
                if self._maze[i][j] == 0:
                    lin = self.check_neighbours(j, i)

                    if lin is not None:
                        self._nodes.update({(j, i): lin})

