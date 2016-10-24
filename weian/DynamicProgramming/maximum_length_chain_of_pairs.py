#!/usr/bin/env python3

"""
"
" Author : Weian Cheng
"
" Dynamic Programming
" Set 20. Maximum Length Chain of Pairs
" http://www.geeksforgeeks.org/
"        dynamic-programming-set-20-maximum-length-chain-of-pairs/
"
"""

import input_data.dynamic_programming.maximum_length_chain_of_pairs


def maximum_length_chain_of_pairs(pairs):
    counts = len(pairs)
    result = [1 for _ in range(counts)]
    result_pairs = [[] for _ in range(counts)]

    for i in range(counts):
        result_pairs[i].append(pairs[i])
        for j in range(i+1, counts):
            if pairs[i][1] < pairs[j][0]:
                result[j] = max(result[j], result[i]+1)

    maximum = -1
    for _ in result:
        maximum = max(maximum, _)

    return maximum


def main():
    pairs = input_data.dynamic_programming.maximum_length_chain_of_pairs. \
        input_source

    for _ in pairs:
        print("input pairs: " + str(_))
        max_length = maximum_length_chain_of_pairs(_)
        print("maximum length chain of pairs: " + str(max_length))
        print("\n")

if __name__ == "__main__":
    main()
