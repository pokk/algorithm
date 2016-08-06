#!/usr/bin/env python3

"""
"
" Dynamic Programming
" http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
" Set 31. Optimal Strategy for a Game
"
" Author: Weian Cheng
" Date: 8/6/2016
"
"""


def optimal_strategy(array):
    array_len = len(array)
    dp_table = [[(0, 0) for _ in range(array_len)] for _ in range(array_len)]

    for _ in range(array_len):
        dp_table[_][_] = (array[_], 0)

    for length in range(1, array_len+1):
        i = 0
        j = i + length
        while j < array_len:
            if array[i] + dp_table[i+1][j][1] >= array[j] + dp_table[i][j-1][1]:
                dp_table[i][j] = (array[i], dp_table[i+1][j][0])
            else:
                dp_table[i][j] = (array[j], dp_table[i][j-1][0])

            i += 1
            j = i + length

    return dp_table


def maximum_value(table, array):
    t = [_ for _ in range(array)]
    i = 0
    j = array - 1
    steps = []
    print(t)
    print(t.index(4))
    #print(t.pop(4))
    print(t)
    while len(t) != 0:
        #i =
        steps.append(table[i][j])


# not finished yet.
def main():
    array1 = [7, 10, 5, 8, 20, 11, 35, 2]
    array2 = [8, 15, 3, 7]
    t = optimal_strategy(array2)
    print(t)

if __name__ == '__main__':
    main()
