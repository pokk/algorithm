""" Created by Jieyi on 2/14/16. """
from data_structure.binary_tree import BinaryTree
from data_structure.queue import Queue


class DFS:
    """
    Depth first search.
    """

    def __init__(self):
        self.__list_dfs_value = []
        self.__list_dfs_node = []

    def dfs(self, node):
        def inner_dfs(node):
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

            self.__list_dfs_value.append(node.data)
            self.__list_dfs_node.append(node)

            for p in tmp_arr:
                inner_dfs(p)

        self.__init__()
        inner_dfs(node)

    @property
    def dfs_list(self):
        return self.__list_dfs_value

    @property
    def dfs_node_list(self):
        return self.__list_dfs_node


class BFS:
    """
    Breath first search.
    """

    def __init__(self):
        self.__q = Queue()
        self.__list_bfs_val = []
        self.__list_bfs_node = []

    def bfs(self, node):
        def inner_bfs(node):
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

            self.__list_bfs_val.append(node.data)
            self.__list_bfs_node.append(node)

            while not self.__q.is_empty():
                inner_bfs(self.__q.dequeue())

        self.__init__()
        inner_bfs(node)

    @property
    def bfs_list(self):
        return self.__list_bfs_val

    @property
    def bfs_node_list(self):
        return self.__list_bfs_node


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
    bt.add(6)
    bt.add(3)
    bt.add(10)
    bt.add(2)
    bt.add(5)
    bt.add(1)
    bt.add(14)
    bt.show()

    print('--------------------- bfs start -----------------------')

    bfs = BFS()
    bfs.bfs(bt.head)
    print(bfs.bfs_list)

    print('--------------------- dfs start -----------------------')

    dfs = DFS()
    dfs.dfs(bt.head)
    print(dfs.dfs_list)

if __name__ == '__main__':
    main()
