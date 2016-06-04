""" Created by wu.jieyi on 2016/03/23. """
import copy
import sys

from jieyi.algorithm.graph import arr_map


def bellman_ford(path_map, start=0):
    """
    NOTE: This algorithm's limitation is cycle's path total couldn't be minus value.

    :param path_map: A direction graph.
    :param start: The beginning vertex.
    :return: The shortest path.
    """

    def changed_vertex(original, changed):
        """
        Check which index is different between two arrays.
        """

        return [True if original[c] is not changed[c] else False for c in range(len(original))]

    arr_shortest_path = [sys.maxsize] * len(path_map)
    arr_tmp = path_map[start]

    # Total time is all of the vertex number.
    for i in range(len(path_map)):
        # Check which number is different from previous.
        arr_changed = changed_vertex(arr_shortest_path, arr_tmp)
        arr_shortest_path = arr_tmp[:]
        # Looking for the different between this time and previous time.
        for c in range(len(arr_changed)):
            # When we find the different from previous time.
            if arr_changed[c]:
                # The vertices' path length changed re-calculate from it to other vertices which it could go.
                for m in range(len(path_map[c])):
                    # The vertex changed goes to others which it could go that the distance is shorter than itself.
                    if path_map[c][m] + arr_tmp[c] < arr_tmp[m]:
                        # After re-calculate, we save into temporal array.
                        arr_tmp[m] = path_map[c][m] + arr_tmp[c]

    return arr_tmp


def main():
    start = 3
    shortest_path = bellman_ford(copy.deepcopy(arr_map), start)

    for i in range(len(shortest_path)):
        if start is not i:
            print(start, '->', i, 'length:', shortest_path[i])


if __name__ == '__main__':
    main()
