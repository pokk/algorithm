#!/usr/bin/env python3

"""
"
" Author : Weian Cheng
"
" Dynamic Programming
" Set 28 Minimum insertions to form a palindrome
" http://www.geeksforgeeks.org/
"        dynamic-programming-set-28-minimum-insertions-to-form-a-palindrome/
"
"""

import input_data.dynamic_programming.minimum_insertions_palindrome

INF = float("INF")


def is_palindrome(string):
    if len(string) <= 1:
        return True

    length = len(string)

    middle = int(length/2 if length % 2 == 0 else length/2 + 1)

    for _ in range(middle):
        if string[_] != string[length - 1 - _]:
            return False

    return True


def remove_palindrome(string):
    length = len(string)
    middle = int(length/2 if length % 2 == 0 else length/2 + 1)

    start = 0
    end = length-1

    for _ in range(middle):
        e = length - 1 - _
        if string[_] == string[e] and _ != e:
            start = _ + 1
            end = e

    return string[start:end]


def minimum_insertions_palindrome(string):
    length = len(string)
    palindrome_table = [[0 for _ in range(length)] for _ in range(length)]

    string = remove_palindrome(string)

    for l in range(1, length):
        for i in range(length-l):
            if is_palindrome(string[i:i+l+1]):
                palindrome_table[i][i+l] = 0
                continue

            minimum = INF
            for _ in range(i, i+l):
                minimum = min(minimum, 1 + palindrome_table[i][_] +
                              palindrome_table[_+1][i+l])

            palindrome_table[i][i+l] = minimum

    return palindrome_table[0][length-1]


def main():
    input_source = input_data.dynamic_programming.\
        minimum_insertions_palindrome.input_source

    for string in input_source:
        print("input string: " + string)
        palindrome = minimum_insertions_palindrome(string)
        print("minimum insertions palindrome: " + str(palindrome))
        print("")

if __name__ == "__main__":
    main()
