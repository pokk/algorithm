""" Created by Jieyi on 06/09/2016. """
from input_data.dynamic_programming.longest_increasing_subsequence import input_source
from jieyi.algorithm.dynamic_programming import DP


class LIS(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
    """

    def __init__(self, sequence):
        self._seq = sequence
        self._length_list_of_seq = [0 for _ in sequence]

    def _find_max_length_index(self, len_list_of_seq):
        return -1 if len(len_list_of_seq) == 0 else self._length_list_of_seq.index(max(len_list_of_seq))

    def _less_than(self, cur_index, cur_value):
        return [self._length_list_of_seq[i] for i in range(cur_index) if cur_value > self._seq[i]]

    def _algorithm(self):
        for i, v in enumerate(self._seq):
            if i == 0:
                self._length_list_of_seq[i] = 1  # Initialize the first one length.
            else:
                less_than = self._less_than(i, self._seq[i])
                longest_index = self._find_max_length_index(less_than)
                self._length_list_of_seq[i] = 1 if longest_index == -1 else self._length_list_of_seq[longest_index] + 1

    def _backtracking(self):
        seq = []
        max_len = max(self._length_list_of_seq)
        for i in range(len(self._length_list_of_seq) - 1, -1, -1):
            if max_len == self._length_list_of_seq[i]:
                seq.append(self._seq[i])
                max_len -= 1

        return seq

    def res(self):
        self._algorithm()
        seq = self._backtracking()
        seq.reverse()

        return max(self._length_list_of_seq), ' '.join(str(s) for s in seq)


def main():
    for lis in input_source:
        l = LIS(lis)
        print(l.res())


if __name__ == '__main__':
    main()
