#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Dynamic Programming
" Minimum number of jumps to reach end
"
" http://www.geeksforgeeks.org/
"        minimum-number-of-jumps-to-reach-end-of-a-given-array/
"
"""

import input_data.dynamic_programming.minimum_number_of_jumps_to_reach_end

INF = float("inf")


def minimum_number_of_jumps_to_reach_end(array):
    steps = [INF] * len(array)

    steps[0] = 0
    result = [-1] * len(array)
    for now in range(len(array)-1):
        if not array[now]:
            continue

        for index in range(1, array[now]+1):
            if steps[index+now] > steps[now] + 1:
                result[now+index] = now
            steps[index+now] = min(steps[index+now], steps[now] + 1)
            if index + now + 1 >= len(array):
                break

    path = print_path(result, array)
    return steps[len(array)-1], path


def print_path(trace, array):
    index = len(array) - 1
    path = []
    while True:
        path.append(array[index])
        index = trace[index]
        if index == -1:
            break

    path.reverse()
    return path


def main():
    sources = input_data.dynamic_programming\
        .minimum_number_of_jumps_to_reach_end.input_sources

    for array in sources:
        jumps, path = minimum_number_of_jumps_to_reach_end(array)
        info = str(path[0])
        for i in range(1, len(path)):
            info = "%s->%s" % (info, path[i])

        print("Input: arr[] = " + str(array))
        print("Output: " + str(jumps) + " (" + info + ")")
        print("\n")


if __name__ == '__main__':
    main()
