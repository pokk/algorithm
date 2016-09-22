#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" http://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/
"
"""

INF = float("INF")


def bellman_ford(matrix, length):
    distance = [INF for _ in range(length)]
    parent = [None for _ in range(length)]

    distance[0] = 0

    for _ in range(length - 1):
        for i in range(length):
            for j in range(length):
                if distance[i] != INF and matrix[i][j] != INF:
                    if distance[i] + matrix[i][j] < distance[j]:
                        distance[j] = distance[i] + matrix[i][j]
                        parent[j] = i

    return distance, parent

def main():
    path = [[0, 10, 3, INF, INF, INF],
            [INF, 0, INF, 2, -3, INF],
            [INF, INF, 0, INF, 3, INF],
            [INF, -1, INF, 0, INF, INF],
            [INF, INF, INF, 4, 0, 1],
            [INF, INF, INF, 4, INF,0]]

    d, p = bellman_ford(path, 6)

    print("distance: ")
    print(d)
    print("parent: ")
    print(p)

if __name__ == "__main__":
    main()
