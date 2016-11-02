#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Dynamic Programming
" Set 1. Longest Palindrome Substring
"
" http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
"
"""

import input_data.dynamic_programming.longest_palindromic_subsequence


def longest_palindrome_substring(string):
    string_len = len(string)
    if string_len == 0:
        return None

    dp_table = [[False for _ in range(string_len)] for _ in range(string_len)]

    for i in range(string_len):
        dp_table[i][i] = True

    i = 0
    max_length = 0
    for length in range(2, string_len+1):
        for start in range(string_len-length+1):
            end = start + length - 1
            substring = string[start:end+1]
            if substring[0:1] == substring[len(substring)-1:len(substring)]:
                if length == 2:
                    dp_table[start][end] = True
                else:
                    if dp_table[start+1][end-1]:
                        dp_table[start][end] = True
                        if max_length < length:
                            max_length = length
                            i = start

    return string[i:i+max_length]


def main():
    strings = input_data.dynamic_programming.longest_palindromic_subsequence\
        .input_source

    for string in strings:
        print("input string: " + string)
        substring = longest_palindrome_substring(string)
        print("Longest palindrome substring is: " + substring)
        print("Length is: " + str(len(substring)))
        print("\n")


if __name__ == "__main__":
    main()
