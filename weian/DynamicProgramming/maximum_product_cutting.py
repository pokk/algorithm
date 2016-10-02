#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Dynamic Programming
" Set 36. Maximum Product Cutting
" http://www.geeksforgeeks.org/
"        dynamic-programming-set-36-cut-a-rope-to-maximize-product/
"
"""

import input_data.dynamic_programming.maximum_product_cutting


def maximum_product_cutting(length):
    result = [0] * (length+1)

    result[2] = 1

    for i in range(3, length+1):
        for j in range(1, int(i/2)+1):
            result[i] = max(result[j], j) * max(result[i-j], i-j)

    return result[length-1]

def main():
    lengths = input_data.dynamic_programming.maximum_product_cutting.\
        rope_lengths

    for length in lengths:
        result = maximum_product_cutting(length)
        print("rope length: " + str(length))
        print("Maximum product is " + str(result))
        print("\n")

if __name__ == "__main__":
    main()
