""" Created by Jieyi on 2/11/16. """
from data_structure.__interface__ import BinaryTreeNode


class BinaryTree:
    def __init__(self):
        self._head = None

    def add_node(self, obj):
        if self._head is None:
            self._head = BinaryTreeNode(obj)
            return

        th = self._head
        while 1:
            if obj > th.data:
                if th.right is not None:
                    th = th.right
                else:
                    th.right = BinaryTreeNode(obj)
                    return
            elif obj < th.data:
                if th.left is not None:
                    th = th.left
                else:
                    th.left = BinaryTreeNode(obj)
                    return

    def show(self):
        # self._in_order(self._head)
        self._pre_order(self._head)

    def _pre_order(self, node):
        if node:
            print(node.data)
            self._pre_order(node.left)
            self._pre_order(node.right)

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.data)
            self._in_order(node.right)

    def _post_order(self, node):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.data)

    @property
    def head(self):
        return self._head


def main():
    bt = BinaryTree()
    bt.add_node(1)
    bt.add_node(3)
    bt.add_node(0)
    bt.add_node(4)

    bt.show()


if __name__ == '__main__':
    main()
