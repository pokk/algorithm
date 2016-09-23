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

INF = float("inf")


def word_wrap_problem(string, width):
    string_split = string.split(" ")
    string_count = []
    for index in range(len(string_split)):
        string_count.append(len(string_split[index]))

    dp_table = [[INF for _ in range(len(string_count))] for _ in range(len(
        string_count))]

    for i in range(len(string_count)):
        dp_table[i][i] = width - string_count[i]

    for length in range(1, len(string_count)):
        for i in range(len(string_count)-length):
            if sum(string_count[i:i+length+1])+length == width:
                dp_table[i][i+length] = 0
                print(str(i) + " " + str(i+length))
                continue

            for j in range(i, i+length):
                print("[" + str(i) + "][" + str(j) + "] [" + str(j+1) + "]["
                      + str(i+length) + "]")
                dp_table[i][i+length] = min(dp_table[i][i+length], dp_table[i][j] + dp_table[j+1][i+length])

    print(string_count)
    print(dp_table)


def main():
    string = "aaa bb cc ddddd"
    word_wrap_problem(string, 6)

if __name__ == "__main__":
    main()
