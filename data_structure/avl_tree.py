""" Created by wu.jieyi on 2016/02/24. """
from data_structure.binary_tree import BinaryTree


class AVLTree(BinaryTree):
    def __init__(self):
        super(AVLTree, self).__init__()

    def add(self, obj):
        super().add(obj)
        self.__cal_height(self.head)

    def del_node(self, node):
        pass

    def __cal_height(self, node):
        """
        Calculate the height of each node of whole tree.

        :param node: The tree head.
        """
        if node:
            node.height = self.height(node.left) - self.height(node.right)
            self.__cal_height(node.left)
            self.__cal_height(node.right)


def main():
    print("hello world")
    arr = [1, 3, 0, 4]

    avl_tree = AVLTree()
    for num in arr:
        avl_tree.add(num)

    avl_tree.show()


if __name__ == '__main__':
    main()
