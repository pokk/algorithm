""" Created by Jieyi on 9/2/16. """
from collections import OrderedDict
from collections import deque
from copy import deepcopy

from input_data.dynamic_programming.box_stacking_problem import input_source
from jieyi.algorithm.dynamic_programming import DP


class BSP(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/
    """

    def __init__(self, rectangles):
        self.__arr_rects = rectangles
        self.__arr_order_rects = None
        self.__arr_res = []

    def _preset(self):
        # Calculate all of rolling rectangles.
        tmp = []
        for rect in self.__arr_rects:
            t = deque(rect)
            for _ in range(len(t)):
                t.rotate(1)
                tmp.append(list(t))
        self.__arr_rects = tmp

        # Order by rectangle area and length, width.
        self.__arr_order_rects = OrderedDict.fromkeys(sorted([rect[0] * rect[1] for rect in self.__arr_rects]), 1)
        for rect in self.__arr_rects:
            item = rect.pop()
            tmp = sorted(rect)
            tmp.append(item)
            self.__arr_order_rects[rect[0] * rect[1]] = tmp
        print(self.__arr_order_rects)

        self.__arr_res = [rect[2] for _, rect in self.__arr_order_rects.items()]
        # Change the dict's key to order key.
        tmp = deepcopy(self.__arr_order_rects)
        self.__arr_order_rects = OrderedDict.fromkeys([_ for _ in range(len(tmp))])
        index = 0
        for _, value in tmp.items():
            self.__arr_order_rects[index] = value
            index += 1

    def _algorithm(self):
        for i in range(len(self.__arr_order_rects)):
            for j in range(i):
                if self.__arr_order_rects[j][0] < self.__arr_order_rects[i][0] and self.__arr_order_rects[j][1] < self.__arr_order_rects[i][1]:
                    if self.__arr_res[j] + self.__arr_order_rects[i][2] > self.__arr_res[i]:
                        self.__arr_res[i] = self.__arr_res[j] + self.__arr_order_rects[i][2]

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        self._algorithm()

        return max(self.__arr_res)


def main():
    for inp in input_source:
        c = BSP(inp)
        print(c.res())


if __name__ == '__main__':
    main()
