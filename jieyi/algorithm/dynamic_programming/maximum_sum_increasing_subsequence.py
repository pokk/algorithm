""" Created by Jieyi on 8/28/16. """

from input_data.dynamic_programming.maximum_sum_increasing_subsequence import input_source
from jieyi.algorithm.dynamic_programming import DP


class MSIS(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-14-maximum-sum-increasing-subsequence/
    """
    def __init__(self, array):
        self._arr_list = array
        self._arr_value = self._arr_list[:]
        self._arr_index = [i for i in range(len(self._arr_list))]

    def _preset(self):
        pass

    def _algorithm(self):
        for i in range(len(self._arr_list)):
            for j in range(i):
                if self._arr_list[j] < self._arr_list[i]:
                    self._arr_value[i] = self._arr_value[i] + self._arr_list[j]

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        self._algorithm()

        return max(self._arr_value)


def main():
    for inp in input_source:
        c = MSIS(inp)
        print(c.res())


if __name__ == '__main__':
    main()
