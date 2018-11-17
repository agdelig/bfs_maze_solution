import os

from app.find_path import BFSMaze


def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    start = tuple(lines[0].replace('\n', '').split(' '))
    start = tuple(map(int, start))

    end = tuple(lines[1].replace('\n', '').split(' '))
    end = tuple(map(int, end))

    maze = []
    for i in range(2, len(lines)):
        line = list(lines[i].replace('\n', '').split(' '))
        maze.append(list(map(int, line)))

    bfs_maze = BFSMaze(maze=maze,start=start, end=end)
    path = bfs_maze.search()

    print('\nOUTPUT\n')

    if path is not None:
        print_outcome(maze, path, start, end)
    else:
        print('Could not reach end point!')


def print_outcome(maze, path, start, end):
    for node in path:
        maze[node[1]][node[0]] = 4

    maze[start[1]][start[0]] = 2
    maze[end[1]][end[0]] = 3

    for line in maze:

        l = ['#' if x == 1
             else 'X' if x == 4
             else ' ' if x == 0
             else 'S' if x == 2
             else 'E' if x == 3
             else None
             for x in line]

        print(*l, sep='')


def start_search():

    while True:
        file_path = input('\nPlease enter file path or type exit to exit:')
        if file_path == 'exit':
            exit(0)
        elif os.path.exists(file_path) \
                and os.path.isfile(file_path) \
                and file_path.endswith('.txt'):
            read_file(file_path)
        else:
            print(f'There seems to be a problem with file "{file_path}"!')


