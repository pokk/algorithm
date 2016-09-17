#!/usr/bin/env python3

"""
"
" Author : Weian Cheng
"
" Dynamic Programming
" Set 22. Box Stacking Problem
" http://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/
"
"""

import input_data.dynamic_programming.box_stacking_problem


def list_rotation(input_list, rotate_count):
    count = rotate_count % 4
    return input_list[-count:] + input_list[:-count]


def get_all_boxes(boxes):
    all_boxes = []

    for _ in boxes:
        all_boxes.append(_)
        for i in range(1, len(_)):
            all_boxes.append(list_rotation(_, i))

    return all_boxes


def sorting_boxes_by_area(all_boxes):
    sorted_boxes = []

    for _ in all_boxes:
        sorted_boxes.insert(_[1]*_[2], _)

    sorted_boxes.sort(key=lambda x: x[1]*x[2])
    return sorted_boxes


def longest_increasing_subsequence(boxes):
    length = len(boxes)
    result = [1 for _ in range(length)]
    result_height = []

    for _ in boxes:
        result_height.append(_[0])

    for i in range(length):
        for j in range(i+1, length):
            if boxes[i][1] < boxes[j][1] and boxes[i][2] < boxes[j][2]:
                if result[j] < result[i]+1:
                    result[j] = result[i] + 1
                    result_height[j] = result_height[i] + boxes[j][0]

    maximum = -1
    for _ in result_height:
        maximum = max(maximum, _)

    return maximum


def box_stacking_problem(boxes):
    maximum_height = longest_increasing_subsequence(
        sorting_boxes_by_area(get_all_boxes(boxes)))

    return maximum_height


def main():
    # height x length x width
    boxes = input_data.dynamic_programming.box_stacking_problem.input_source

    for _ in boxes:
        r = box_stacking_problem(_)
        print(_)
        print("maximum height: " + str(r))
        print("\n")

if __name__ == "__main__":
    main()
