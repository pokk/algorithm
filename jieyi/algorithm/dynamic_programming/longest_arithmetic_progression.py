""" Created by jieyi on 2016/10/24. """
from input_data.dynamic_programming.longest_arithmetic_progression import input_source
from jieyi.algorithm.dynamic_programming import DP


class LLAP(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/length-of-the-longest-arithmatic-progression-in-a-sorted-array/
    """

    def __init__(self, array):
        self._array = array
        self._ans_arr = [1 for _ in range(len(self._array))]

    def _preset(self):
        pass

    def _algorithm(self):
        """
        There are three numbers, a = 1, b = 4, c = 7.
        We can obtain a formula is "b x 2 = a + c", so we're using this concept to count.

        :return: the longest arithmetic progression.
        """

        if len(self._array) <= 2:
            return len(self._array)

        for i in range(len(self._array)):
            for j in range(i + 1, len(self._array)):
                for k in range(j + 1, len(self._array)):
                    if self._array[j] * 2 - self._array[i] == self._array[k]:
                        self._ans_arr[k] = max(self._ans_arr[k], self._ans_arr[j] + 1)

        return max(self._ans_arr) + 1

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    for inp in input_source:
        c = LLAP(inp)
        print(c.res())


if __name__ == '__main__':
    main()
