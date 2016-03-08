""" Created by wu.jieyi on 2016/02/24. """
from data_structure.__interface__ import AvlTreeNode
from data_structure.binary_tree import BinaryTree
from data_structure.stack import Stack


class AVLTree(BinaryTree):
    def __init__(self):
        super(AVLTree, self).__init__()

        self.__stack = Stack()

    def add(self, obj):
        def inner_add(node, inner_obj):
            self.__stack.push(node)
            if inner_obj > node.data:
                if not node.right:
                    node.right = AvlTreeNode(inner_obj)
                    node.right.parent = node
                else:
                    inner_add(node.right, inner_obj)
            elif inner_obj < node.data:
                if not node.left:
                    node.left = AvlTreeNode(inner_obj)
                    node.left.parent = node
                else:
                    inner_add(node.left, inner_obj)

        # If the head is null.
        if not self._head:
            self._head = AvlTreeNode(obj)
        else:
            inner_add(self._head, obj)

        # Re-balance and calculate height and balance factory for each passed node.
        while 1:
            re_node = self.__stack.pop()
            if not re_node:
                break
            re_node.height = self.height(re_node)
            re_node.balance_factor = self.__balance_facotr(re_node)

            # Here is problem node.
            if abs(re_node.balance_factor) is 2:
                self.__re_balance(re_node)
                # Reset all of the node height and balance factor.
                self.__reset_tree_height_factor(self._head)

    def del_node(self, node):
        del_node = self._find(node)
        del_node_parent = del_node.parent if del_node.parent else None

        if not super(AVLTree, self).del_node(node):
            return False

        # Reset whole tree from the node we wanna delete.
        self.__reset_tree_height_factor(del_node_parent)
        # TODO: Re-balance. Check it from leaves.

        return True

    def __reset_tree_height_factor(self, node):
        """
        Re-calculate each node of tree's height and balance factor from node.

        :param node: Start from node.
        """

        if node:
            self.__reset_tree_height_factor(node.left)
            self.__reset_tree_height_factor(node.right)
            node.height = self.height(node)
            node.balance_factor = self.__balance_facotr(node)

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
        self._re_connect_child(node_parent, y)

    def __balance_facotr(self, node):
        if not node.left and not node.right:
            return 0
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1
        return left_height - right_height


def main():
    arr = [7, 4, 8, 5, 1, 3, 6]
    avl_tree = AVLTree()
    for num in arr:
        avl_tree.add(num)

    avl_tree.show()

    avl_tree.del_node(4)
    print('=========delete==========')
    avl_tree.show()


if __name__ == '__main__':
    main()
