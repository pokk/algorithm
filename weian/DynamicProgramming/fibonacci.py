#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Dynamic Programming
"
" Fibonacci Number
"
"""


def fibonacci_recursive(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_dp(n):
    dp_table = [1 for _ in range(n)]

    for i in range(2, n):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    return dp_table[n-1]


def main():
    n = 13

    print("Fibonacci number with dynamic programing: " + str(fibonacci_dp(n)))
    print("Fibonacci number with recursive: " + str(fibonacci_recursive(n)))

if __name__ == "__main__":
    main()
