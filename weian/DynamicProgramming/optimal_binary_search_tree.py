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

    for _ in range(length):
        cost[_][_] = frequency[_]

    for l in range(2, length+1):
        for i in range(length - l + 1):
            j = i + l - 1
            m = INF
            for k in range(i, j):
                print(m)
                m = min(m, cost[i][k-1] + cost[k+1][j])
                print(m)


            print("i: " + str(i) + " j: " + str(j) + " m: " + str(m) + " sum: " + str(freq_sum(frequency, i, l)))
            s = m + freq_sum(frequency, i, l)
            cost[i][j] = s

    print(cost)


def main():
    #f = [4, 2, 6, 3]
    f = [34, 8, 50]
    OBST(f)

if __name__ == "__main__":
    main()
