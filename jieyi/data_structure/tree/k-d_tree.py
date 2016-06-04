""" Created by wu.jieyi on 2016/03/29. """
from operator import itemgetter

from jieyi.data_structure import BinaryTreeNode


class KDTree:
    def __init__(self, data_arr):
        self._head = None
        self._data_arr = data_arr
        self.dim = len(data_arr[0])

    def create(self):
        """
        K-Dimension tree is a binary tree.
        We compare the number in each of the level as like a binary tree.
        """

        def inner_create(data, depth=0):
            if len(data) is 0:
                return None

            d = sorted(data, key=itemgetter(depth % self.dim))

            # Create a node and assign the middle of number into node's data.
            node = BinaryTreeNode(d[int(len(d) / 2)])
            # The array of the left recursive in the left branch.
            node.left = inner_create(d[:int(len(d) / 2)], depth + 1)
            # The array of the right recursive in the right branch.
            node.right = inner_create(d[int(len(d) / 2) + 1:], depth + 1)

            return node

        self._head = inner_create(self._data_arr)

    def show(self):
        self._in_order(self._head)

    def _in_order(self, node):
        if node:
            print(node)
            self._in_order(node.left)
            self._in_order(node.right)


def main():
    d = [(3, 5), (1, 6), (2, 4), (1, 7), (6, 3), (9, 4), (7, 4), (6, 2), (8, 8), (9, 7)]
    kd = KDTree(d)
    kd.create()
    kd.show()


if __name__ == '__main__':
    main()
