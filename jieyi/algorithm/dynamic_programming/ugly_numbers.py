""" Created by Jieyi on 10/18/16. """
from input_data.dynamic_programming.ugly_numbers import input_source
from jieyi.algorithm.dynamic_programming import DP


class UN(DP):
    """
    Dynamic Programming
    http://www.geeksforgeeks.org/ugly-numbers/
    """

    def __init__(self, number):
        self._number = number
        self._arr = [0] * 2
        self._real_arr = []

    def _preset(self):
        self._arr[0] = 0
        self._arr[1] = 1

    def _algorithm(self):
        i = 1
        while True:
            if self._number <= len(self._real_arr):
                break
            if self._arr[i] == 1:
                if self._number > len(self._real_arr):
                    self._arr += [0] * (i * 5 - len(self._real_arr))
                    self._arr[i * 2] = 1
                    self._arr[i * 3] = 1
                    self._arr[i * 5] = 1
                    self._real_arr.append(i)
            i += 1

        return self._real_arr[self._number - 1]

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    for inp in input_source:
        c = UN(inp)
        print(c.res())


if __name__ == '__main__':
    main()
