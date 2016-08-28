#!/usr/bin/env python

INF = float("INF")


def warshall(graph, path_graph, length):
    distance = [[INF for _ in range(length)] for _ in range(length)]
    path = [[None for _ in range(length)] for _ in range(length)]

    for i in range(length):
        for j in range(length):
            distance[i][j] = graph[i][j]
            path[i][j] = path_graph[i][j]

    for k in range(length):
        for i in range(length):
            for j in range(length):
                if distance[i][k] == INF or distance[k][j] == INF:
                    continue
                elif distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    path[i][j] = path[k][j]

    print(distance)
    print(path)


def main():
    inf = float("INF")
    graph = [[0, 3, 6, 15],
             [inf, 0, -2, inf],
             [inf, inf, 0, 2],
             [1, 4, inf, 0]]

    graph2 = [[inf, 5, 1, 2],
              [5, inf, 3, inf],
              [1, 3, inf, 4],
              [2, inf, 4, inf]]

    path = [[None, 0, 0, 0],
            [None, None, 1, None],
            [None, None, None, 2],
            [3, None, 3, None]]

    warshall(graph, path, 4)

if __name__ == "__main__":
    main()
