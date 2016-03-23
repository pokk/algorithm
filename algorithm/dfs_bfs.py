""" Created by Jieyi on 2/14/16. """
from data_structure.queue import Queue
from data_structure.tree.binary_tree import BinaryTree


class DFS:
    """
    Depth first search.
    """

    def __init__(self):
        self.__list_dfs_value = []
        self.__list_dfs_node = []

    def dfs(self, node):
        def inner_dfs(inner_node):
            """ Algorithm
            1. Collate all of the children of the node into array.
            2. Save the node content into array list.
            3. Recursive DFS algorithm from children array.
            4. Got an sequence of DFS order.

            :param inner_node: Now we're visiting node.
            """

            tmp_arr = []

            if inner_node.left:
                tmp_arr.append(inner_node.left)
            if inner_node.right:
                tmp_arr.append(inner_node.right)

            self.__list_dfs_value.append(inner_node.data)
            self.__list_dfs_node.append(inner_node)

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
        def inner_bfs(inner_node):
            """ Algorithm
            1. Put all of the children of the node into a queue.
            2. Save the node content into array list.
            3. Recursive BFS algorithm by using the first of queue head node.
            4. Got an sequence of BFS order.

            :param inner_node: Now we're visiting node.
            """

            if inner_node.left:
                self.__q.enqueue(inner_node.left)
            if inner_node.right:
                self.__q.enqueue(inner_node.right)

            self.__list_bfs_val.append(inner_node.data)
            self.__list_bfs_node.append(inner_node)

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
    arr = [6, 3, 10, 2, 5, 1, 14]
    bt = BinaryTree()
    for num in arr:
        bt.add(num)
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
