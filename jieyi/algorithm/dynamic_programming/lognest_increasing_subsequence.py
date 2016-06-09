""" Created by Jieyi on 06/09/2016. """
from input_data.dynamic_programming.longest_increasing_subsequence import lis_str2


class LIS:
    def __init__(self, sequence):
        self._seq = sequence
        self._length_list_of_seq = [0 for _ in sequence]

    def _lis_len(self):
        pass

    def _lis_algorithm(self):
        for i, v in enumerate(self._seq):
            if i == 0:
                self._length_list_of_seq[i] = 1
            else:
                longest_index = self._find_max_length_index(self._length_list_of_seq)
                less_than = self._less_than(i, self._seq[i])
                self._length_list_of_seq[i] = self._length_list_of_seq[longest_index] + 1
                # return self._length_list_of_seq

    def _find_max_length_index(self, len_list_of_seq):
        return self._length_list_of_seq.index(max(len_list_of_seq))

    def _less_than(self, cur_index, cur_value):
        less_than_index_list = []
        for i in range(cur_index):
            if cur_value > self._seq[i]:
                less_than_index_list.append(i)

        return less_than_index_list

    def res(self):
        self._lis_algorithm()

        return self._length_list_of_seq


def main():
    lis = LIS(lis_str2)
    print(lis_str2)
    print(lis.res())


if __name__ == '__main__':
    main()
