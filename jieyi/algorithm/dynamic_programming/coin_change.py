""" Created by Jieyi on 8/25/16. """
from input_data.dynamic_programming.coin_change import input_source
from jieyi.algorithm.dynamic_programming import DP


class CC(DP):
    def __init__(self, money, price):
        self._total_money = money
        self._arr_price = price
        self._res_matrix = [[0 for _ in range(self._total_money + 1)] for _ in range(len(self._arr_price) + 1)]

    def _preset(self):
        pass

    def _algorithm(self):
        for i in range(1, len(self._arr_price) + 1):
            for j in range(1, self._total_money + 1):
                self._res_matrix[i][j] = self._res_matrix[i - 1][j] + {
                    j < self._arr_price[i - 1]: 0,
                    j == self._arr_price[i - 1]: 1,
                    j > self._arr_price[i - 1]: self._res_matrix[i][j - self._arr_price[i - 1]]
                }.get(True)

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        self._algorithm()

        return self._res_matrix[len(self._arr_price)][self._total_money]


def main():
    for inp in input_source:
        c = CC(inp[0], inp[1])
        print(c.res())


if __name__ == '__main__':
    main()
