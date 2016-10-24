""" Created by jieyi on 2016/10/24. """
from input_data.dynamic_programming.largest_sum_contiguous_subarray import input_source
from jieyi.algorithm.dynamic_programming import DP


class LSCS(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
    """

    def __init__(self, array):
        self._array = array
        self._ans_arr = [0 for _ in range(len(array))]
        self._max_sum = 0

    def _preset(self):
        pass

    def _algorithm(self):
        curr_number = 0
        for i in range(len(self._array)):
            self._ans_arr[i] = max(0, curr_number + self._array[i])
            # Keep the previous number.
            curr_number = self._ans_arr[i]
            # Keep the maximum number.
            self._max_sum = max(self._max_sum, curr_number)

        return self._max_sum

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    for inp in input_source:
        c = LSCS(inp)
        print(c.res())


if __name__ == '__main__':
    main()
