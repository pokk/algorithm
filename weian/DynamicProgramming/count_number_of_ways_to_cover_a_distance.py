#!/usr/bin/python3

"""
http://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
"""
from input_data.dynamic_programming.way_to_cover_distance import n1
from input_data.dynamic_programming.way_to_cover_distance import n2
from input_data.dynamic_programming.way_to_cover_distance import n3
from input_data.dynamic_programming.way_to_cover_distance import n4


def count_by_recurrence(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 4

    return count_by_recurrence(n-1) + count_by_recurrence(n-2) + \
           count_by_recurrence(n-3)


def count_by_dynamic_programming(n):
    if n == 0:
        return 1

    count = [0] * n

    count[0] = 1
    count[1] = 2
    count[2] = 4

    for i in range(3, n):
        count[i] = count[i-1] + count[i-2] + count[i-3]

    return count[n-1]


def main():
    print(count_by_recurrence(n1))
    print(count_by_dynamic_programming(n4))

if __name__ == '__main__':
    main()
