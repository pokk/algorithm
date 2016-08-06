#!/usr/bin/env python3

"""
"
" Dynamic Programming
" http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/
" Set 6. Min Cost Path
"
" Author: Weian Cheng
" Date: 8/6/2016
"
"""

def min_cost_path(array, ii, jj):
    # initial table
    dp_table = [[float("inf") for _ in range(jj+1)] for _ in range(ii+1)]

    for i in range(1, ii+1):
        for j in range(1, jj+1):
            minimum = min(dp_table[i-1][j],
                          dp_table[i][j-1],
                          dp_table[i-1][j-1])
            if minimum == float("inf"):
                dp_table[i][j] = array[i-1][j-1]
            else:
                dp_table[i][j] = minimum + array[i-1][j-1]

    result = []

    i = ii
    j = jj

    while True:
        result.insert(0, (i-1, j-1))
        m = min(dp_table[i-1][j], dp_table[i][j-1], dp_table[i-1][j-1])
        if m == dp_table[i-1][j]:
            i -= 1
        elif m == dp_table[i][j-1]:
            j -= 1
        else:
            i -= 1
            j -= 1

        if i == 0 or j == 0:
            break

    return dp_table[ii][jj], result

def main():
    array = [[1, 2, 3],
             [4, 8, 2],
             [1, 5, 3]]

    cost, path = min_cost_path(array, 3, 3)

    print("path: ")
    print(path)
    print("min cost: " + str(cost))

if __name__ == '__main__':
    main()
