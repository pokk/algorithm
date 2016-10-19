""" Created by Jieyi on 06/22/2016. """
from input_data.dynamic_programming.way_to_cover_distance import input_source
from jieyi.algorithm.dynamic_programming import DP


class WaysToCoverDistance(DP):
    """
    Count number of ways to cover a distance.
    It's kind of the Fibonacci sequence.
    The problem's description is as below.
    http://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
    """

    def __init__(self, n):
        self._answer_step = [0, 1, 2, 4]
        self._step = n

    def _algorithm(self):
        if self._step < 2:
            return self._answer_step[self._step]

        for i in range(4, self._step + 1):
            self._answer_step.append(self._answer_step[i - 1] + self._answer_step[i - 2] + self._answer_step[i - 3])

        return self._answer_step[self._step]

    def _backtracking(self):
        pass

    def res(self):
        return self._algorithm()


def main():
    for wtcd in input_source:
        w = WaysToCoverDistance(wtcd)
        print(w.res())


if __name__ == '__main__':
    main()
