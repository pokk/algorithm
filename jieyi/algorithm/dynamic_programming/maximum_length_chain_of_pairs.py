""" Created by jieyi on 2016/10/24. """
from input_data.dynamic_programming.maximum_length_chain_of_pairs import input_source
from jieyi.algorithm.dynamic_programming import DP


class MLCP(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-20-maximum-length-chain-of-pairs/
    """

    def __init__(self, array):
        self._array = array
        self._ans_arr = [1 for _ in range(len(self._array))]

    def _preset(self):
        pass

    def _algorithm(self):
        for i in range(1, len(self._array)):
            for j in range(i):
                if self._array[j][1] < self._array[i][0]:
                    self._ans_arr[i] = max(self._ans_arr[i], self._ans_arr[j] + 1)

        return max(self._ans_arr)

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    for inp in input_source:
        c = MLCP(inp)
        print(c.res())


if __name__ == '__main__':
    main()
