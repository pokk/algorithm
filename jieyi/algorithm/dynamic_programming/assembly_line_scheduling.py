""" Created by Jieyi on 10/22/16. """
import sys

from input_data.dynamic_programming.assembly_line_scheduling import input_source
from jieyi.algorithm.dynamic_programming import DP


class ALS(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-34-assembly-line-scheduling/
    """

    def __init__(self, input_data):
        self._top_stations = [input_data[2][0][0]] + input_data[0][0] + [input_data[2][1][0]]
        self._bottom_stations = [input_data[2][0][1]] + input_data[0][1] + [input_data[2][1][1]]
        self._top_to_bottom_cost = [sys.maxsize] + input_data[1][0] + [sys.maxsize]
        self._bottom_to_top_cost = [sys.maxsize] + input_data[1][1] + [sys.maxsize]

        self._top_output = [input_data[2][0][0]]
        self._bottom_output = [input_data[2][0][1]]

    def _preset(self):
        pass

    def _algorithm(self):
        for i in range(len(self._top_stations) - 1):
            self._top_output.append(min(self._top_output[i] + self._top_stations[i + 1],
                                        self._bottom_output[i] + self._bottom_to_top_cost[i] + self._top_stations[i + 1]))
            self._bottom_output.append(min(self._bottom_output[i] + self._bottom_stations[i + 1],
                                           self._top_output[i] + self._top_to_bottom_cost[i] + self._bottom_stations[i + 1]))

        return min(self._top_output[-1], self._bottom_output[-1])

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    for inp in input_source:
        c = ALS(inp)
        print(c.res())


if __name__ == '__main__':
    main()
