""" Created by Jieyi on 8/21/16. """
import sys

INF = sys.maxsize
map1 = [[0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]]
map2 = [[0, 4, 2, INF, INF, INF],
        [1, 0, INF, 2, INF, INF],
        [INF, 3, 0, INF, 5, INF],
        [INF, INF, 4, 0, INF, 2],
        [INF, INF, INF, 1, 0, INF],
        [INF, 4, 5, INF, 3, 0]]

input_source = [map1, map2]
