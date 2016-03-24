""" Created by wu.jieyi on 2016/03/23. """
import copy

from algorithm.graph.__init__ import arr_map


def floyd_warshall(path_map):
    """
    This is following to Floyd–Warshall algorithm. All path the shortest path.
    """

    for k in range(len(path_map)):
        for i in range(len(path_map)):
            for j in range(len(path_map)):
                if path_map[i][j] > path_map[i][k] + path_map[k][j]:
                    path_map[i][j] = path_map[i][k] + path_map[k][j]

    return path_map


def main():
    all_shortest_path = floyd_warshall(copy.deepcopy(arr_map))

    for i in range(len(all_shortest_path)):
        for j in range(len(all_shortest_path[i])):
            if all_shortest_path[i][j] is not 0:
                print(i, '->', j, 'length:', all_shortest_path[i][j], end=', ' if j < len(all_shortest_path[i]) - 1 else '\n')


if __name__ == '__main__':
    main()
