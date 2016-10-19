""" Created by Jieyi on 9/9/16. """
from input_data.dynamic_programming.partition_problem import input_source
from jieyi.algorithm.dynamic_programming import DP


class PP(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
    """

    def __init__(self, input_arr):
        self._input_list = sorted(input_arr)
        self._res_table = []

    def _preset(self):
        pass

    def _algorithm(self):
        if sum(self._input_list) % 2 == 1:
            return False
        else:
            self._res_table = [[True] + [False for _ in range(int(sum(self._input_list) / 2))] for _ in range(len(self._input_list))]

            for i in range(len(self._input_list)):
                for j in range(1, len(self._res_table[0])):
                    if i == 0:
                        if self._input_list[i] == j:
                            self._res_table[i][j] = True
                    else:
                        if self._res_table[i - 1][j]:
                            self._res_table[i][j] = True
                        else:
                            if self._res_table[i - 1][j - self._input_list[i]]:
                                self._res_table[i][j] = True

            return self._res_table[len(self._res_table) - 1][len(self._res_table[0]) - 1]

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    for inp in input_source:
        c = PP(inp)
        print(c.res())


if __name__ == '__main__':
    main()
