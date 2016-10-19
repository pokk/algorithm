#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Dynamic Programming
" Set 11. Egg Dropping Puzzle
" http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
"
"""

INF = float("inf")

def egg_dropping_puzzle(floor_num, egg_num):
    dp_table = [[0 for _ in range(floor_num+1)] for _ in range(egg_num+1)]

    for i in range(floor_num+1):
        dp_table[1][i] = i

    for egg in range(2, egg_num+1):
        for floor in range(1, floor_num+1):
            # print("floor: " + str(floor))
            minimum = INF
            for count_floor in range(1, floor+1):
                minimum = min(minimum, 1+max(dp_table[egg-1][count_floor-1],
                                             dp_table[egg][floor-count_floor]))
                # print("count_floor: " + str(count_floor))
                # print("dp_table[" + str(floor-count_floor) + "] = " + str(dp_table[egg][floor-count_floor]))
                # print("minimum: " + str(minimum))
            dp_table[egg][floor] = minimum

    # for e in range(egg_num+1):
    #    print(dp_table[e])
    return str(dp_table[egg_num][floor_num])

def main():
    floors_number = 100
    eggs_number = 2
    result = egg_dropping_puzzle(floors_number, eggs_number)

    print("Building height: " + str(floors_number))
    print("Eggs: " + str(eggs_number))
    print("minimized dropping: " + str(result))

if __name__ == "__main__":
    main()
