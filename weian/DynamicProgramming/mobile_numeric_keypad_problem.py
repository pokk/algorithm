#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Dynamic Programming
" Mobile Numeric Keypad Problem
"
" http://www.geeksforgeeks.org/mobile-numeric-keypad-problem/
"
"""


def mobile_numeric_keypad_problem(n):
    if n < 1:
        return 0

    keypad = [[0, 8],  # 0
              [1, 2, 4],  # 1
              [1, 2, 3, 5],  # 2
              [2, 3, 6],  # 3
              [1, 4, 5, 7],  # 4
              [2, 4, 5, 6, 8],  # 5
              [3, 5, 6, 9],  # 6
              [4, 7, 8],  # 7
              [0, 5, 7, 8, 9],  # 8
              [6, 8, 9]]  # 9

    # dp_table = [[1] * 10] * n
    dp_table = [[1 for _ in range(10)] for _ in range(n)]

    for i in range(1, n):
        for j in range(10):
            s = 0
            for k in keypad[j]:
                s += dp_table[i-1][k]
            dp_table[i][j] = s

    return sum(dp_table[n-1])


def main():
    n = 5

    for i in range(1, n+1):
        print("Count for numbers of length " + str(i) + ": " +
              str(mobile_numeric_keypad_problem(i)))

if __name__ == "__main__":
    main()
