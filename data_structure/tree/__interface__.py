""" Created by wu.jieyi on 2016/03/23. """


class BinaryTreeNode:
    def __init__(self, obj):
        self.parent = None
        self.left = None
        self.data = obj
        self.height = 0
        self.right = None

    def __str__(self):
        return 'data: %s \t,parent: %s  \t,l-child: %s \t,r-child: %s \t,height: %s' \
               % (self.data,
                  self.parent.data if self.parent else None,
                  self.left.data if self.left else None,
                  self.right.data if self.right else None,
                  self.height)


class AvlTreeNode(BinaryTreeNode):
    def __init__(self, obj):
        super().__init__(obj)
        self.balance_factor = 0

    def __str__(self):
        return 'data: %s \t,parent: %s  \t,l-child: %s \t,r-child: %s \t,height: %s \t,b_factor: %s' \
               % (self.data,
                  self.parent.data if self.parent else None,
                  self.left.data if self.left else None,
                  self.right.data if self.right else None,
                  self.height,
                  self.balance_factor)


def main():
    print("hello world")


if __name__ == '__main__':
    main()
