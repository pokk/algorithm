""" Created by Jieyi on 7/6/16. """
from input_data.dynamic_programming.subset_sum_problem import input_source
from jieyi.algorithm.dynamic_programming import DP


class SubsetSumProblem(DP):
    def __init__(self, set_list, max_total):
        self._list = set_list
        self._total = max_total
        self._matrix = [[False for _ in range(max_total + 1)] for _ in range(len(set_list) + 1)]

    def _preset(self):
        for i in range(len(self._matrix)):
            self._matrix[i][0] = True

    def _algorithm(self):
        for i in range(1, len(self._matrix)):
            for j in range(1, len(self._matrix[i])):
                if j < self._list[i - 1]:
                    self._matrix[i][j] = self._matrix[i - 1][j]
                else:
                    self._matrix[i][j] = self._matrix[i - 1][j] or self._matrix[i - 1][j - self._list[i - 1]]

    def _backtracking(self):
        # TODO: I haven't programmed backtracking function for finding the subset.
        pass

    def res(self):
        self._preset()
        self._algorithm()

        for i in range(len(self._matrix)):
            if self._matrix[i][len(self._matrix[i]) - 1]:
                return True
        return False
        # for i, _ in enumerate(self._matrix):
        #     print(self._list[i - 1], _)


def main():
    for ssp in input_source:
        c = SubsetSumProblem(ssp[0], ssp[1])
        print(c.res())


if __name__ == '__main__':
    main()
