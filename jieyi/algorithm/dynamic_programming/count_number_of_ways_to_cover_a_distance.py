""" Created by jieyi on 2016/10/24. """
from jieyi.algorithm.dynamic_programming import DP


class CNWCD(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
    """

    def __init__(self, n):
        self._n = n
        self._ans_arr = [0, 1, 2, 4]

    def _preset(self):
        pass

    def _algorithm(self):
        for i in range(4, self._n + 1):
            self._ans_arr.append(self._ans_arr[i - 1] + self._ans_arr[i - 2] + self._ans_arr[i - 3])

        return self._ans_arr[self._n]

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    input_source = [6, 21, 104, 62]
    for inp in input_source:
        c = CNWCD(inp)
        print(c.res())


if __name__ == '__main__':
    main()
