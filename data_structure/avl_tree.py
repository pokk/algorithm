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
                else:
                    inner_add(node.right, obj)
            elif obj < node.data:
                if not node.left:
                    node.left = AvlTreeNode(obj)
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
            if abs(re_node.balance_factor) is 2:
                self.__rotate(re_node)
                # TODO: select the head and parent.

    def del_node(self, node):
        pass

    def __cal_balance_facotr(self, node):
        """
        """

        if not node.left and not node.right:
            return 0
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1
        return left_height - right_height

    def __rotate(self, node):
        if node.balance_factor is 2:
            if node.left.balance_factor is 1:
                self.__ll_rotate(node)
            elif node.left.balance_factor is -1:
                self.__lr_rotate(node)
            pass
        elif node.balance_factor is -2:
            if node.right.balance_factor is 1:
                self.__rl_rotate(node)
            elif node.right.balance_factor is -1:
                self.__rr_rotate(node)
            pass
        pass

    def __ll_rotate(self, node):
        """
               z                                      y
              / \                                   /   \
             y   T4      Right Rotate (z)          x      z
            / \          - - - - - - - - ->      /  \    /  \
           x   T3                               T1  T2  T3  T4
          / \
        T1   T2
        """

        a = node
        b = node.left
        a.left = b.right
        b.right = a
        print('ll')

    def __rr_rotate(self, node):
        """
             z                               z                           x
            / \                            /   \                        /  \
           y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
          / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
        T1   x                          y    T3                    T1  T2 T3  T4
            / \                        / \
          T2   T3                    T1   T2
        """

        a = node
        b = node.right
        a.right = b.left
        b.left = a
        print('rr')

    def __lr_rotate(self, node):
        """
          z                                y
         /  \                            /   \
        T1   y     Left Rotate(z)       z      x
            /  \   - - - - - - - ->    / \    / \
           T2   x                     T1  T2 T3  T4
               / \
             T3  T4
        """

        a = node
        b = node.left
        c = node.left.right

        a.left = c.right
        b.right = c.left
        c.right = a
        c.left = b
        print('lr')

    def __rl_rotate(self, node):
        """
           z                            z                            x
          / \                          / \                          /  \
        T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
            / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
           x   T4                      T2   y                  T1  T2  T3  T4
          / \                              /  \
        T2   T3                           T3   T4
        """

        a = node
        b = node.right
        c = node.right.left

        a.right = c.left
        b.left = c.right
        c.left = a
        c.right = b
        print('rl')


def main():
    arr = [4, 2, 6, 8, 9]

    avl_tree = AVLTree()
    for num in arr:
        avl_tree.add(num)

    avl_tree.show()


if __name__ == '__main__':
    main()
