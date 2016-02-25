""" Created by Jieyi on 2/14/16. """
from data_structure.binary_tree import BinaryTree
from data_structure.queue import Queue


class DFS:
    """
    Depth first search.
    """

    def __init__(self):
        self.__arr_list = []

    def dfs(self, node):
        """ Algorithm
        1. Collate all of the children of the node into array.
        2. Save the node content into array list.
        3. Recursive DFS algorithm from children array.
        4. Got an sequence of DFS order.

        :param node: Now we're visiting node.
        """

        tmp_arr = []

        if node.left is not None:
            tmp_arr.append(node.left)
        if node.right is not None:
            tmp_arr.append(node.right)

        self.__arr_list.append(node.data)

        for p in tmp_arr:
            self.dfs(p)

    @property
    def get_dfs_list(self):
        return self.__arr_list


class BFS:
    """
    Breath first search.
    """

    def __init__(self):
        self.__q = Queue()
        self.__arr_list = []

    def bfs(self, node):
        """ Algorithm
        1. Put all of the children of the node into a queue.
        2. Save the node content into array list.
        3. Recursive BFS algorithm by using the first of queue head node.
        4. Got an sequence of BFS order.

        :param node: Now we're visiting node.
        """

        if node.left is not None:
            self.__q.enqueue(node.left)
        if node.right is not None:
            self.__q.enqueue(node.right)

        self.__arr_list.append(node.data)

        while not self.__q.is_empty():
            self.bfs(self.__q.dequeue())

    @property
    def bfs_list(self):
        return self.__arr_list


def main():
    """
    binary tree:
             6
            / \
           3  10
          / \   \
         2   5  14
        /
       1
    """

    bt = BinaryTree()
    bt.add_node(6)
    bt.add_node(3)
    bt.add_node(10)
    bt.add_node(2)
    bt.add_node(5)
    bt.add_node(1)
    bt.add_node(14)
    bt.show()

    print('--------------------- bfs start -----------------------')

    bfs = BFS()
    bfs.bfs(bt.head)
    print(bfs.bfs_list)

    print('--------------------- dfs start -----------------------')

    dfs = DFS()
    dfs.dfs(bt.head)
    print(dfs.get_dfs_list)


if __name__ == '__main__':
    main()
