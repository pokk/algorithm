#!/usr/bin/env python3

"""
"
" Author : Weian Cheng
"
" Dynamic Programming
" Set 32. Word Break Problem
" http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/
"
"""

import input_data.dynamic_programming.word_break_problem


def print_list(table):
    for i in range(len(table)):
        print(table[i])


def is_word_in_dict(w, dictionary):
    if dictionary.count(w) != 0:
        return True

    for d in dictionary:
        if w is d[0]:
            return True

    return False


def word_break_problem(word, dictionary):
    length = len(word)
    dp_table = [[False for _ in range(length)] for _ in range(length)]
    back_track = [[None for _ in range(length)] for _ in range(length)]

    for scan_len in range(length):
        # print("length: " + str(scan_len))
        for word_len in range(length-scan_len):
            string = word[word_len:word_len+scan_len+1]
            # print("string: " + string)
            if is_word_in_dict(string, dictionary):
                dp_table[word_len][word_len+scan_len] = True
                back_track[word_len][word_len+scan_len] = -1
                continue

            for index in range(word_len, word_len+scan_len):
                # print("[" + str(word_len) + "][" + str(index) + "] [" + str(
                #    index+1) + "][" + str(word_len+scan_len) + "]")
                if dp_table[word_len][index] and dp_table[index+1][
                            word_len+scan_len]:
                    dp_table[word_len][word_len+scan_len] = True
                    back_track[word_len][word_len+scan_len] = index - word_len
                    break

    # print_list(dp_table)
    # print_list(back_track)
    words = back_tracking(dp_table, back_track, word, dictionary)
    return words


def back_tracking(dp_table, back_track_table, string, dictionary):
    if not dp_table[0][len(string)-1]:
        return None
    head = 0
    tail = len(string) - 1
    segment = []

    while True:
        index = back_track_table[head][tail]
        if index == -1:
            segment.append(string[head:tail+1])
            break

        if is_word_in_dict(string[head:head+index+1], dictionary):
            segment.append(string[head:head+index+1])
            head += index + 1
        elif is_word_in_dict(string[head+index+1:tail+1],
                             dictionary):
            segment.append(string[head+index+1:tail+1])
            tail = head+index

    return segment


def main():
    l = len(input_data.dynamic_programming.word_break_problem.input_word)

    for i in range(l):
        w = input_data.dynamic_programming.word_break_problem.input_word[i]
        d = input_data.dynamic_programming.word_break_problem.input_dict[i]

        result = word_break_problem(w, d)
        print("input data: " + w)
        print("dictionary: " + str(d))
        print("The string can be segmented: " + str(result) if result else
              "The string can not be segmented.")
        print("\n")

if __name__ == "__main__":
    main()
