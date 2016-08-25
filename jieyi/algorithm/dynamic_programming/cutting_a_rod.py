""" Created by Jieyi on 8/25/16. """
from input_data.dynamic_programming.cutting_a_rod import input_source
from jieyi.algorithm.dynamic_programming import DP


class CR(DP):
    def __init__(self, price_arr):
        self._price_array = [0] + price_arr
        self._max_value = self._price_array[:]

    def _preset(self):
        pass

    def _algorithm(self):
        for i in range(len(self._max_value)):
            max_value = 0
            for j in range(i + 1):
                max_value = max(self._price_array[j] + self._max_value[i - j], max_value)
            self._max_value[i] = max_value

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        self._algorithm()

        return self._max_value[-1]


def main():
    for inp in input_source:
        c = CR(inp)
        print(c.res())


if __name__ == '__main__':
    main()
