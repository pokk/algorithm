""" Created by wu.jieyi on 2016/02/24. """
from data_structure.__interface__ import BinaryTreeNode
from data_structure.binary_tree import BinaryTree
from data_structure.queue import Queue


class MaxHeap(BinaryTree):
    def __init__(self):
        super().__init__()
        self.__q = Queue()
        self._finish_add = False

    def add_node(self, obj):
        def add_left_or_right(inner_node, inner):
            if not inner_node.left:
                inner_node.left = BinaryTreeNode(inner)
            elif not inner_node.right:
                inner_node.right = BinaryTreeNode(inner)
            else:
                return False

            self._finish_add = True
            return True

        def dfs_add_node(inner_node, inner):
            # Add a new node to left or right node.
            if add_left_or_right(inner_node, inner):
                return

            # Travel by dfs.
            if inner_node.left:
                self.__q.enqueue(inner_node.left)
            if inner_node.right:
                self.__q.enqueue(inner_node.right)

            while not self.__q.is_empty():
                q = self.__q.dequeue()
                # Decide we need to visit all of node or not.
                if not self._finish_add:
                    dfs_add_node(q, inner)

        if not self._head:
            self._head = BinaryTreeNode(obj)
            return

        self._finish_add = False
        dfs_add_node(self._head, obj)

    def del_node(self):
        pass

    def _re_heap_up(self):
        pass

    def _re_heap_down(self):
        pass


class MinHeap(BinaryTree):
    pass


def main():
    """
              1
            3   2
          6  4 5  9
    """
    mh = MaxHeap()
    mh.add_node(1)
    mh.add_node(3)
    mh.add_node(2)
    mh.add_node(6)
    mh.add_node(4)
    mh.add_node(5)
    mh.add_node(9)
    mh.show()

    a = [1, 2, 3, 4]
    c = [2, 4, 5]


if __name__ == '__main__':
    main()
