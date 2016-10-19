#!/usr/bin/env python3

"""
"
" Author : Weian Cheng
"
" Dynamic Programming
" Set 12. Longest Palindrome Subsequence
" http://www.geeksforgeeks.org/
"        dynamic-programming-set-12-longest-palindromic-subsequence/
"
"""

import input_data.dynamic_programming.longest_palindrome_subsequence


def longest_palindrome_subsequence(sequence):
    length = len(sequence)
    dp_table = [[0 for _ in range(length)] for _ in range(length)]
    backtrack = [[(0, 0) for _ in range(length)] for _ in range(length)]

    for ii in range(length):
        dp_table[ii][ii] = 1

    for l in range(1, length):
        for str_len in range(length-l):
            start = str_len
            end = str_len + l
            sub_str = sequence[start:end+1]

            p_len = 0
            if sub_str[0] == sub_str[len(sub_str)-1]:
                if l == 1:
                    p_len = max(p_len, 2)
                else:
                    if dp_table[start+1][end-1]+2 > p_len:
                        backtrack[start][end] = (start+1, end-1)
                    p_len = max(p_len, dp_table[start+1][end-1]+2)
            else:
                if dp_table[start][end-1] > dp_table[start+1][end]:
                    backtrack[start][end] = (start, end-1)
                else:
                    backtrack[start][end] = (start+1, end)
                p_len = max(p_len,
                            dp_table[start][end-1],
                            dp_table[start+1][end])

            dp_table[start][end] = p_len

    return dp_table[0][length-1]


def main():
    source = input_data.dynamic_programming.lonest_palindrome_subsequence\
        .input_source

    for string in source:
        length = longest_palindrome_subsequence(string)
        print("string: " + string)
        print("longest palindrome subsequence: " + str(length))
        print("\n")

if __name__ == "__main__":
    main()
