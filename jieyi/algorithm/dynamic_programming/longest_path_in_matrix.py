""" Created by Jieyi on 7/3/16. """
from operator import itemgetter

import numpy as np

from input_data.dynamic_programming.longest_path_in_matrix import m1


class LongestPathInMatrix:
    def __init__(self, matrix=None):
        self._matrix = matrix
        self._matrix_dim = (len(self._matrix), len(self._matrix[0]))
        self._number_list = []
        self._record_step_matrix = [[1 for _ in range(len(self._matrix[_]))] for _ in range(len(self._matrix))]
        self._direct = ['up', 'down', 'left', 'right']

    def _preset(self):
        # 2D matrix to 1D list and record their coordination.
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                self._number_list.append({'number': self._matrix[i][j], 'coordinate': (i, j)})
        # sorting by 'number' of each dict.
        self._number_list = sorted(self._number_list, key=itemgetter('number'))

    def _get_coordination_by_direct(self, ori_coordination, dim, direct):
        coord = {
            'up': (ori_coordination[0] - 1, ori_coordination[1]),
            'down': (ori_coordination[0] + 1, ori_coordination[1]),
            'left': (ori_coordination[0], ori_coordination[1] - 1),
            'right': (ori_coordination[0], ori_coordination[1] + 1),
        }.get(direct)

        return coord if 0 <= coord[0] < dim[0] and 0 <= coord[1] < dim[1] else None

    def _algorithm(self):
        for d in self._number_list:
            num = d.get('number')
            coord = d.get('coordinate')  # i: coord[0], j: coord[1]
            for direct in self._direct:
                d_c = self._get_coordination_by_direct(coord, self._matrix_dim, direct)
                if d_c and num + 1 == self._matrix[d_c[0]][d_c[1]]:
                    self._record_step_matrix[d_c[0]][d_c[1]] = self._record_step_matrix[coord[0]][coord[1]] + 1

    def res(self):
        self._preset()
        self._algorithm()
        return max(np.array(self._record_step_matrix).ravel())


def main():
    l = LongestPathInMatrix(m1)
    print(l.res())


if __name__ == '__main__':
    main()
