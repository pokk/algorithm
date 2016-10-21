#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Dynamic Programming
" Largest Sum Contiguous Subarray
"
" https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"
"""

import input_data.dynamic_programming.largest_sum_contiguous_subarray


def largest_sum_contiguous_subarray(array):
    length = len(array)
    begin = 0
    end = 0
    now = 0
    maximum = 0

    for i in range(length):
        now = now + array[i]

        if int(now) < 0:
            begin = i + 1
            end = i + 1
            now = 0

        if maximum < now:
            maximum = now
            end = i

    return maximum, begin, end


def main():
    arrays = input_data.dynamic_programming.\
        largest_sum_contiguous_subarray.array

    for array in arrays:
        m, b, e = largest_sum_contiguous_subarray(array)

        i = 0
        is_print = False
        subarray = []
        for value in array:
            if i == b:
                is_print = True

            if is_print:
                subarray.append(value)

            if i == e:
                is_print = False

            i += 1

        print(array)
        print("maximum sum: " + str(m))
        print(subarray)
        print("\n")

if __name__ == "__main__":
    main()
