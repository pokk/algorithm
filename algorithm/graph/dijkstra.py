""" Created by wu.jieyi on 2016/03/23. """
import copy
import sys

from algorithm.graph.__init__ import arr_map


def dijkstra(path_map, start=0):
    """
    This is following to Dijkstra's algorithm. The shortest path of single vertex to all vertex.
    ** NOTE: This algorithm's limitation is the path cannot be minus value.

    :param start: The beginning vertex.
    :param path_map: A direction graph.
    """

    arr_shortest_path = path_map[start]
    stack = []

    # Until all vertices put into stack.
    while 1:
        if len(stack) is len(arr_shortest_path):
            break

        # Pick the smallest value from the arr_shortest_path is not including vertices in the stack.
        tmp_arr = arr_shortest_path[:]
        for i in range(len(stack)):
            tmp_arr[stack[i]] = sys.maxsize
        mini_vertex = arr_shortest_path.index(min(tmp_arr))
        stack.append(mini_vertex)

        # Calculate the smallest value's vertex with all vertices which it could go.
        for i in range(len(arr_shortest_path)):
            if arr_shortest_path[i] > arr_shortest_path[mini_vertex] + path_map[mini_vertex][i]:
                arr_shortest_path[i] = arr_shortest_path[mini_vertex] + path_map[mini_vertex][i]

    return arr_shortest_path


def main():
    start = 3
    shortest_path = dijkstra(copy.deepcopy(arr_map), start)

    for i in range(len(shortest_path)):
        if start is not i:
            print(start, '->', i, 'length:', shortest_path[i])


if __name__ == '__main__':
    main()
