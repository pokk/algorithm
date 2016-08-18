#!/usr/bin/env python3

"""
"
" Dynamic Programming
" http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
" Set 3. Longest Increasing Subsequence
"
" Author: Weian Cheng
" Date: 8/6/2016
"
"""

def LIS(array):
    result = []
    candidate = []

    for i in array:
        # handle first item.
        if len(result) == 0:
            result.append(i)
            continue

        if result[len(result)-1] < i:
            result.append(i)
            continue

        if i < result[len(result)-1]:
            if i >= result[len(result) - 2]:
                result[len(result)-1] = i

            if len(candidate) > 0:
                candidate.append(i)
                if len(candidate) > len(result):
                    result = candidate[:]
                    candidate.clear()
                    continue

            if i < result[0] and len(candidate) == 0:
                candidate.append(i)

    return result


def main():
    #array1 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    #array = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    #print(LIS(array1))

    array = []
    t = input("T: ")
    n = input("N: ")
    for _ in range(int(t)):
        a = input("array: ")
        array.append(int(i) for i in a.split())

    for _ in array:
        print("LIS: " + str(len(LIS(_))))


if __name__ == '__main__':
    main()
