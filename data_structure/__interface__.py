""" Created by Jieyi on 2/24/16. """


class BinaryTreeNode:
    def __init__(self, obj):
        self.parent = None
        self.left = None
        self.data = obj
        self.right = None

    # def __str__(self):
    #     return '(parent: %s, data: %s, l-child: %s, r-child: %s)' % (self.parent, str(self.data), self.left, self.right)

    def show(self):
        print('(parent: %s, data: %s, l-child: %s, r-child: %s)' % (self.parent, str(self.data), self.left, self.right))


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
