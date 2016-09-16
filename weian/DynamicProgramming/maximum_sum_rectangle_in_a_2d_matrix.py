#!/usr/bin/env python3

"""
"
" Author : Weian Cheng
"
" Dynamic Programming
" Set 27
" http://www.geeksforgeeks.org/
"        dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/
"
"""

import input_data.dynamic_programming.maximum_sum_rectangle_in_a_2d_matrix


def find_max_sum(matrix):
    length = len(matrix)
    max_sum = 0
    max_start = 0
    max_end = 0
    end = 0

    for i in range(length):
        s = 0
        start = i
        for j in range(i, length):
            if matrix[j] + s > 0:
                s += matrix[j]
                end = j
            elif matrix[j] + s < 0:
                start = end = j
                s = matrix[j]

            if s > max_sum:
                max_sum = s
                max_start = start
                max_end = end

    return max_start, max_end, max_sum


def maximum_sum_rectangle_in_2d_matrix(matrix, i, j):
    max_sum = 0
    max_left = 0
    max_right = 0
    max_up = 0
    max_down = 0

    zero = [0 for _ in range(j)]

    for l in range(i):
        current_sum = zero[:]
        for r in range(l, i):
            for _ in range(j):
                current_sum[_] += matrix[_][r]

            start, end, s = find_max_sum(current_sum)
            if s > max_sum:
                max_sum = s
                max_left = l
                max_right = r
                max_up = start
                max_down = end

    return max_sum, max_left, max_right, max_up, max_down


def main():
    data = input_data.dynamic_programming.maximum_sum_rectangle_in_a_2d_matrix.\
        input_matrix

    for _ in data:
        s, l, r, u, d = maximum_sum_rectangle_in_2d_matrix(_, 5, 4)
        print(_)
        print("maximum sum: " + str(s))
        print("left: " + str(l) + " right: " + str(r))
        print("up: " + str(u) + " down: " + str(d))
        print("\n")

if __name__ == "__main__":
    main()
