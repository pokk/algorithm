""" Created by Jieyi on 2/11/16. """
from data_structure.__interface__ import BinaryTreeNode


class BinaryTree:
    def __init__(self):
        self._head = None

    def add(self, obj):
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

    def find(self, obj):
        res = self._find(obj)
        return res.data if res else None

    def height(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def show(self):
        # self._in_order(self._head)
        self._pre_order(self._head)

    def _find(self, obj):
        res = None

        def search_bt(node):
            if node:
                if node.data is obj:
                    nonlocal res
                    res = node
                    return
                search_bt(node.left)
                search_bt(node.right)

        search_bt(self._head)
        return res

    def _pre_order(self, node):
        if node:
            print(node)
            self._pre_order(node.left)
            self._pre_order(node.right)

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node)
            self._in_order(node.right)

    def _post_order(self, node):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node)

    @property
    def head(self):
        return self._head


def main():
    bt = BinaryTree()
    bt.add(1)
    bt.add(3)
    bt.add(0)
    bt.add(4)

    bt.show()


if __name__ == '__main__':
    main()
