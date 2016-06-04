""" Created by Jieyi on 2/11/16. """
from jieyi.data_structure import BinaryTreeNode
from jieyi.data_structure import Stack


class BinaryTree:
    def __init__(self):
        self.__stack = Stack()
        self._head = None

    def add(self, obj):
        def inner_add(inner_obj):
            if self._head is None:
                self._head = BinaryTreeNode(inner_obj)
                return

            th = self._head
            while 1:
                self.__stack.push(th)
                if inner_obj > th.data:
                    if th.right is not None:
                        th = th.right
                    else:
                        th.right = BinaryTreeNode(inner_obj)
                        th.right.parent = th
                        return
                elif inner_obj < th.data:
                    if th.left is not None:
                        th = th.left
                    else:
                        th.left = BinaryTreeNode(inner_obj)
                        th.left.parent = th
                        return

        inner_add(obj)

        while 1:
            n = self.__stack.pop()
            if not n:
                break
            n.height = self.height(n)

    def find(self, obj):
        res = self._find(obj)
        return res.data if res else None

    def del_node(self, node):
        del_node = self._find(node)
        if not del_node:
            return False

        del_node_parent = del_node.parent if del_node.parent else None

        # No children tree.
        if not del_node.left and not del_node.right:
            pass
        # No left child tree then catch the right child tree.
        elif not del_node.left:
            self._re_connect_child(del_node_parent, del_node.right)
        # There are children tree. Change the biggest node of left child tree.
        else:
            biggest_node = self._find_biggest(del_node.left)
            del_node.data, biggest_node.data = biggest_node.data, del_node.data
            # Assign for deleting.
            del_node_parent, del_node = biggest_node.parent, biggest_node

        self._del_child(del_node_parent, del_node)

        return True

    def height(self, node):
        if not node or (not node.left and not node.right):
            return 0
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return max(left_height, right_height) + 1

    def show(self):
        # self._in_order(self._head)
        self._pre_order(self._head)
        # self._post_order(self._head)

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

    def _find_biggest(self, node):
        if node.right:
            return self._find_biggest(node.right)
        else:
            return node

    def _del_child(self, parent, child):
        child.parent = None
        if parent.left is child:
            parent.left = None
        elif parent.right is child:
            parent.right = None

        del child

    def _re_connect_child(self, parent, new_node):
        if parent:
            if parent.data > new_node.data:
                parent.left = new_node
                new_node.parent = parent
            else:
                parent.right = new_node
                new_node.parent = parent
        else:
            new_node.parent = None
            self._head = new_node

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
    arr = [1, 3, 0, 4, 2, 5, 6]
    bt = BinaryTree()
    for num in arr:
        bt.add(num)

    bt.show()

    bt.del_node(1)

    print('===================================')
    bt.show()


if __name__ == '__main__':
    main()
