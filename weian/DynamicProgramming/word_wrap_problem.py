#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Dynamic Programming
" Set 19. Word Wrap Problem
" http://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/
"
"""

import input_data.dynamic_programming.word_wrap_problem

INF = float("inf")


def word_wrap_problem(string_len, width):
    length = len(string_len)
    cost_table = [[INF for _ in range(length)] for _ in range(length)]

    for i in range(length):
        for j in range(i, length):
            cost = sum(string_len[i:j+1]) + (j-i)
            cost_table[i][j] = (width-cost)**2 if cost <= width else INF

    cost = [INF for _ in range(length)]
    backtrack = [0 for _ in range(length)]

    cost[0] = cost_table[0][0]

    for l in range(1, length):
        minimum = INF
        for i in range(l+1):
            if i == l:
                if minimum > cost_table[0][i]:
                    backtrack[l] = 0
                minimum = min(minimum, cost_table[0][i])
            else:
                if minimum > cost[i] + cost_table[i+1][l]:
                    backtrack[l] = i+1
                minimum = min(minimum, cost[i] + cost_table[i+1][l])

        cost[l] = minimum

    back_tracking(backtrack, length)

    return cost[length-1]

def back_tracking(p, n):
    now = n - 1
    while now >= 0:
        print(str(p[now]) + " pointer to " + str(now))
        if now <= 0:
            break
        elif p[now] == now:
            now = now - 1
            continue
        else:
            now = p[now] - 1

def main():
    datas = input_data.dynamic_programming.word_wrap_problem.input_source

    for data in datas:
        string = data[0]
        width = data[1]
        word_wrap_problem(string, width)
        print("\n")

if __name__ == "__main__":
    main()
