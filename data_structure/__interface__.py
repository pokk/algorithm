""" Created by Jieyi on 2/24/16. """


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


class LinkedListNode:
    def __init__(self, obj):
        self.previous = None
        self.data = obj
        self.next = None

    def __str__(self):
        return str(self.data)


def main():
    print("hello world")


if __name__ == '__main__':
    main()
