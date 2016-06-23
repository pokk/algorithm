#!/usr/bin/python3

from input_data.dynamic_programming.longest_increasing_subsequence import lis_str2


def lis(string):
    string_len = len(string)
    length = [1] * string_len

    for i in range(string_len):
        for j in range(i, string_len):
            if string[i] < string[j]:
                length[j] = max(length[i] + 1, length[j])

    max_length = length[0]
    for _ in length[1:]:
        if max_length < _:
            max_length = _

    print(trace(string, length, max_length))

    return max_length

# not finish yet, I want to list all subsequence...
def trace(string_list, length_list, lis_length):
    length = len(length_list)

    if lis_length == 1:
        print("no subsequence")
        return None

    subsequence = []
    sub = []

    for i in range(length):
        if length_list[i] != 1:
            break
        same_way = -1
        sub[:] = []
        sub.append(string_list[i])
        for j in range(i, length):
            if length_list[i] == length_list[j]:
                continue
            if length_list[j] > same_way and length_list[j] > length_list[i]:
                same_way = length_list[j]
                sub.append(string_list[j])
                print("push " + str(string_list[j]))
                print("same_way " + str(same_way) + " ; length_list[" + str(j) + "] " + str(length_list[j]))

        subsequence.append(sub)

    return subsequence


def main():
    # print(str(lis([8, 5, 3, 2, 10, 9])))
    print("Max LIS length: " + str(lis(lis_str2)))

if __name__ == '__main__':
    main()