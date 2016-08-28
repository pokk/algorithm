#!/usr/bin/env python


def Warshall(graph, length):
    distance = [[float("INF") for _ in range(length)] for _ in range(length)]
    path = [[None for _ in range(length)] for _ in range(length)]

    for i in range(length):
        for j in range(length):
            distance[i][j] = graph[i][j]
            if i == j:
                path[i][j] = None
            else:
                path[i][j] = j + 1

    print(path)

    for k in range(length):
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                elif distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    path[i][j] = path[j][k]

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
    Warshall(graph2, 4)

if __name__ == "__main__":
    main()
