""" Created by Jieyi on 10/19/16. """
from input_data.dynamic_programming.fibonacci_sequence import input_source
from jieyi.algorithm.dynamic_programming import DP


class FS(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    """

    def __init__(self, number):
        self._number = number
        self._arr = [0, 1, 1]

    def _preset(self):
        pass

    def _algorithm(self):
        for i in range(3, self._number + 1):
            self._arr.append(self._arr[i - 1] + self._arr[i - 2])

        return self._arr[self._number]

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    for inp in input_source:
        c = FS(inp)
        print(c.res())


if __name__ == '__main__':
    main()
