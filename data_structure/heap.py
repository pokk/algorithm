""" Created by wu.jieyi on 2016/02/24. """
from algorithm.dfs_bfs import BFS
from data_structure.__interface__ import BinaryTreeNode
from data_structure.binary_tree import BinaryTree
from data_structure.queue import Queue


class MaxHeap(BinaryTree):
    def __init__(self):
        super().__init__()

        self.__q = Queue()
        self._tail = self._head
        self._finish_add = False

    def add(self, obj):
        self._add_to_balance(obj)
        # Adjust the heap by re-heap-up.
        self._re_heap_up(self._tail)

    def del_node(self, obj=None):
        """
        1. Find the obj you wanna delete.
        2. Change the value from the tail node to the node you wanted to delete.
        3. Delete the tail node then change tail to tail's previous node.
        4. Do re-heap-down from the node you wanted to delete.

        :param obj: the object what you wanted to delete.
        :return: delete obj successfully or not.
        """

        n = self._find(obj)
        if not n:
            return False

        # Step 2.
        n.data = self._tail.data
        # Step 3.
        # Delete the link between the parent and the tail node.
        if self._tail.parent.left and self._tail.parent.left.data is self._tail.data:
            self._tail.parent.left = None
        elif self._tail.parent.right and self._tail.parent.right.data is self._tail.data:
            self._tail.parent.right = None
        del self._tail
        # Reselect a tail node(the tail's previous node).
        self._tail = self._find_tail()
        # Step 4.
        self._re_heap_down(n)

        return True

    def _add_to_balance(self, obj):
        """
        Because of insert into balance tree so we always have to insert
        in the deepest and the rightest position.
        1. Use the similar dfs algorithm for visiting way.
        2. Find the node what we visited has no left child or no right child.
        3. Add the new node there.

        :param obj: What obj we wanna add in.
        """

        def inner_add_l_or_r(inner_node, inner):
            if not inner_node.left:
                self._tail = inner_node.left = BinaryTreeNode(inner)
            elif not inner_node.right:
                self._tail = inner_node.right = BinaryTreeNode(inner)
            else:
                return False

            self._tail.parent = inner_node
            self._finish_add = True

            return True

        def inner_dfs_add_node(inner_node, inner):
            # Add a new node to left or right node.
            if inner_add_l_or_r(inner_node, inner):
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
                    inner_dfs_add_node(q, inner)

        if not self._head:
            self._head = self._tail = BinaryTreeNode(obj)
            return

        self._finish_add = False
        inner_dfs_add_node(self._head, obj)

    def _re_heap_up(self, node):
        """
        Adjust the node as following heap rule from the node to the end.

        :param node: The node is needed to adjust.
        """

        if self.head is not node and node.parent.data < node.data:
            node.parent.data, node.data = node.data, node.parent.data
            self._re_heap_up(node.parent)

    def _re_heap_down(self, node):
        """
        Adjust the node as following heap rule from the node to the end.

        :param node: The node is needed to adjust.
        """

        # No children.
        if not node.left and not node.right:
            return
        # Only left child.
        elif not node.right and node.data < node.left.data:
            changed_node = node.left
        # There are two children.
        else:
            if node.left.data > node.data > node.right.data:
                changed_node = node.left
            elif node.left.data < node.data < node.right.data:
                changed_node = node.right
            elif node.left.data > node.data < node.right.data:
                changed_node = node.left if node.left.data > node.right.data else node.right
            else:
                return

        node.data, changed_node.data = changed_node.data, node.data
        self._re_heap_down(changed_node)

    def _find_tail(self):
        bfs = BFS()
        bfs.bfs(self.head)
        return bfs.bfs_node_list[-1]

    @property
    def tail(self):
        return self._tail


class MinHeap(BinaryTree):
    pass


def main():
    """
        1                      9
      3   2    -> heap ->    4   6
    6  4 5  9              1  3 2  5
    """
    mh = MaxHeap()
    mh.add(1)
    mh.add(3)
    mh.add(2)
    mh.add(6)
    mh.add(4)
    mh.add(5)
    mh.add(9)

    # mh.del_node(4)
    # mh.del_node(9)

    mh.show()


if __name__ == '__main__':
    main()
