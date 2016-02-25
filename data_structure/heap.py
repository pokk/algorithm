""" Created by wu.jieyi on 2016/02/24. """
from data_structure.__interface__ import BinaryTreeNode
from data_structure.queue import Queue
from data_structure.binary_tree import BinaryTree


class MaxHeap(BinaryTree):
    def __init__(self):
        super().__init__()
        self.__q = Queue()

    def add_node(self, obj):
        if not self._head:
            self._head = BinaryTreeNode(obj)
            return

        self.dfs_add_node(self.head, obj)

    # TODO: some problem happened!
    def dfs_add_node(self, node, obj):

        print(node.data)

        if not node.left:
            print('left', node.data, obj)
            node.left = BinaryTreeNode(obj)
            return
        elif not node.right:
            print('right', node.data, obj)
            node.right = BinaryTreeNode(obj)
            return

        if node.left:
            self.__q.enqueue(node.left)
        if node.right:
            self.__q.enqueue(node.right)

        while not self.__q.is_empty():
            self.dfs_add_node(self.__q.dequeue(), obj)


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
    print('===================')
    mh.add_node(3)
    print('===================')
    mh.add_node(2)
    print('===================')
    mh.add_node(6)
    print('===================')
    mh.add_node(4)
    # print('===================')
    # mh.add_node(5)
    # print('===================')
    # mh.add_node(9)
    print('===================')
    mh.show()


if __name__ == '__main__':
    main()
