""" Created by wu.jieyi on 2016/02/24. """
from data_structure.__interface__ import AvlTreeNode
from data_structure.binary_tree import BinaryTree
from data_structure.stack import Stack


class AVLTree(BinaryTree):
    def __init__(self):
        super(AVLTree, self).__init__()

        self.__stack = Stack()

    def add(self, obj):
        def inner_add(node, obj):
            self.__stack.push(node)
            if obj > node.data:
                if not node.right:
                    node.right = AvlTreeNode(obj)
                    node.right.parent = node
                else:
                    inner_add(node.right, obj)
            elif obj < node.data:
                if not node.left:
                    node.left = AvlTreeNode(obj)
                    node.left.parent = node
                else:
                    inner_add(node.left, obj)

        if not self._head:
            self._head = AvlTreeNode(obj)
        else:
            inner_add(self._head, obj)

        while 1:
            re_node = self.__stack.pop()
            if not re_node:
                break
            re_node.height = self.height(re_node)
            re_node.balance_factor = self.__cal_balance_facotr(re_node)

            # Here is problem node.
            if abs(re_node.balance_factor) is 2:
                self.__re_balance(re_node)
                # Reset all of the node height and balance factor.
                self.__reset_tree_height_factor(self._head)

    def del_node(self, node):
        pass

    def __reset_tree_height_factor(self, node):
        if node:
            self.__reset_tree_height_factor(node.left)
            self.__reset_tree_height_factor(node.right)
            node.height = self.height(node)
            node.balance_factor = self.__cal_balance_facotr(node)

    def __cal_balance_facotr(self, node):
        if not node.left and not node.right:
            return 0
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1
        return left_height - right_height

    def __re_balance(self, node):
        if node.balance_factor is 2:
            if node.left.balance_factor is -1:
                # LR rotate.
                self.__rotate(node.left, 'left')
            # RR rotate.
            self.__rotate(node, 'right')
        elif node.balance_factor is -2:
            if node.right.balance_factor is 1:
                # LR rotate.
                self.__rotate(node.right, 'right')
            # LL rotate.
            self.__rotate(node, 'left')

    def __rotate(self, node, l_or_r):
        def inner_left_rotate(inner_node):
            """
              z                                    y
             /  \                                /   \
            T1   y         Left Rotate(z)       z      x
                /  \       - - - - - - - ->    / \    / \
               T2   x                         T1  T2 T3  T4
                   / \
                 T3  T4

            :param inner_node: 'z' node.
            """
            nonlocal y
            inner_node_parent = inner_node.parent
            z = inner_node
            y = inner_node.right
            # Reset the parent.
            if y.left:
                y.left.parent = z
            y.parent = inner_node_parent if inner_node_parent else None
            z.parent = y
            # Rotate.
            z.right = y.left
            y.left = z

        def inner_right_rotate(inner_node):
            """
                   z                                   y
                  / \                                /   \
                 y   T4     Right Rotate(z)         x     z
                / \         - - - - - - - - ->     / \   / \
               x   T3                             T1  T2 T3  T4
              / \
            T1   T2

            :param inner_node: 'z' node.
            """
            nonlocal y
            inner_node_parent = inner_node.parent
            z = inner_node
            y = inner_node.left
            # Reset the parent.
            if y.right:
                y.right.parent = z
            y.parent = inner_node_parent if inner_node_parent else None
            z.parent = y
            # Rotate.
            z.left = y.right
            y.right = z

        node_parent = node.parent
        y = None

        if l_or_r is 'left':
            inner_left_rotate(node)
        elif l_or_r is 'right':
            inner_right_rotate(node)

        # Reset the top of the parent's child.
        if node_parent:
            if node_parent.data > y.data:
                node_parent.left = y
            else:
                node_parent.right = y
        else:
            y.parent = None
            self._head = y


def main():
    arr = [7, 4, 6, 5, 1, 3]
    avl_tree = AVLTree()
    for num in arr:
        avl_tree.add(num)

    avl_tree.show()


if __name__ == '__main__':
    main()
