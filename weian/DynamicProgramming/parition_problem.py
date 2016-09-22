#!/usr/bin/env python3

"""
"
" Author : Weian Cheng
"
" Dynamic Programming
" Set 18. Partition Problem
" http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
"
"""

import input_data.dynamic_programming.partition_problem


def partition_problem(array):
    array = sorted(array)

    if sum(array) % 2 != 0:
        return False

    sub_sum = int(sum(array)/2)

    result_table = [[False for _ in range(sub_sum+1)]
                    for _ in range(len(array))]

    for i in range(len(array)):
        for j in range(1, sub_sum+1):
            if j == array[i]:
                result_table[i][j] = True
                continue

            if i > 0:
                if result_table[i-1][j]:
                    result_table[i][j] = True
                elif j - array[i] > 0:
                    remain = j - array[i]
                    result_table[i][j] = result_table[i-1][remain]

    return result_table[len(array)-1][sub_sum]


def main():
    array = input_data.dynamic_programming.partition_problem.input_source

    for _ in array:
        result = partition_problem(_)
        print(_)
        if result:
            print("Can be divided into two subsets of equal sum")
        else:
            print("Can not be divided into two subsets of equal sum")

        print("\n")

if __name__ == "__main__":
    main()
