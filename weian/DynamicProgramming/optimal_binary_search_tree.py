#!/usr/bin/env python3


INF = float("INF")

def freq_sum(f, i, length):
    s = 0

    for _ in range(length):
        s += f[_ + i]

    return s

def OBST(frequency):
    length = len(frequency)
    cost = [[0 for _ in range(length)] for _ in range(length)]
    path = [[None for _ in range(length)] for _ in range(length)]

    for _ in range(length):
        cost[_][_] = frequency[_]

    for l in range(2, length+1):
        for i in range(length - l + 1):
            j = i + l - 1
            m = INF
            small = 0
            for k in range(i, j+1):
                if k == i:
                    left = 0
                else:
                    left = cost[i][k-1]

                if k == j:
                    right = 0
                else:
                    right = cost[k+1][j]

                if m > left+right:
                    small = k
                m = min(m, left+right)


            s = m + freq_sum(frequency, i, l)
            cost[i][j] = s
            path[i][j] = small

    return cost, path


def main():
    #f = [4, 2, 6, 3]
    f = [34, 8, 50]
    c, p = OBST(f)
    print(c)
    print(p)

if __name__ == "__main__":
    main()
