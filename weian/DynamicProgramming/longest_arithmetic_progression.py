#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Dynamic Programming
" Longest Arithmetic Progression
" http://www.geeksforgeeks.org/
"        length-of-the-longest-arithmatic-progression-in-a-sorted-array/
"
"""

import input_data.dynamic_programming.longest_arithmetic_progression

def longest_arithmetic_progression(sequence):
    length = len(sequence)
    result = [2 for _ in range(length)]

    for index in range(length):
        for i in range(index+1, length):
            for j in range(i+1 , length):
                if sequence[i] * 2 - sequence[index] == sequence[j]:
                    result[j] = max(result[j], result[i] + 1)

    maximum = -1
    for l in result:
        maximum = max(maximum, l)

    return maximum


def main():
    sequences = input_data.dynamic_programming.\
        longest_arithmetic_progression.input_data

    for sequence in sequences:
        print("input data: " + str(sequence))
        print("length of longest arithmetic _progression: " + \
              str(longest_arithmetic_progression(sequence)))
        print("\n")

if __name__ == "__main__":
    main()
