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

        self.__cal_height(self.head)
        while 1:
            re_node = self.__stack.pop()
            if not re_node:
                break
            if abs(re_node.balance_factor) is 2:
                print('you have problem!!!')
                self.__rotate(re_node)
            print(re_node.data, re_node.height)

    def del_node(self, node):
        pass

    def __cal_height(self, node):
        """
        Calculate the height of each node of whole tree.

        :param node: The tree head.
        """
        if node:
            node.balance_factor = self.height(node.left) - self.height(node.right)
            self.__cal_height(node.left)
            self.__cal_height(node.right)

    def __rotate(self, node):
        if node.height is 2:
            print('l')
            if node.right.height is 2:
                pass
            pass
        elif node.height is -2:
            print('r')

            pass
        pass

    def __ll_rotate(self):
        """
               z                                      y
              / \                                   /   \
             y   T4      Right Rotate (z)          x      z
            / \          - - - - - - - - ->      /  \    /  \
           x   T3                               T1  T2  T3  T4
          / \
        T1   T2
        """
        pass

    def __rr_rotate(self):
        """
             z                               z                           x
            / \                            /   \                        /  \
           y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
          / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
        T1   x                          y    T3                    T1  T2 T3  T4
            / \                        / \
          T2   T3                    T1   T2
        """

        pass

    def __lr_rotate(self):
        """
          z                                y
         /  \                            /   \
        T1   y     Left Rotate(z)       z      x
            /  \   - - - - - - - ->    / \    / \
           T2   x                     T1  T2 T3  T4
               / \
             T3  T4
        """

        pass

    def __rl_rotate(self):
        """
           z                            z                            x
          / \                          / \                          /  \
        T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
            / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
           x   T4                      T2   y                  T1  T2  T3  T4
          / \                              /  \
        T2   T3                           T3   T4
        """

        pass


def main():
    arr = [1, 2, 3]

    avl_tree = AVLTree()
    for num in arr:
        avl_tree.add(num)

    avl_tree.show()


if __name__ == '__main__':
    main()
