""" Created by Jieyi on 2/11/16. """


class BT:
    class _Node:
        def __init__(self, obj):
            self.left = None
            self.content = obj
            self.right = None

    def __init__(self):
        self.__head = None

    def add_node(self, obj):
        if self.__head is None:
            self.__head = self._Node(obj)
            return

        th = self.__head
        while True:
            if obj > th.content:
                if th.right is not None:
                    th = th.right
                else:
                    th.right = self._Node(obj)
                    return
            elif obj < th.content:
                if th.left is not None:
                    th = th.left
                else:
                    th.left = self._Node(obj)
                    return

    def show(self):
        self._in_order(self.__head)

    def _in_order(self, node):
        if node is not None:
            self._in_order(node.left)
            print(node.content)
            self._in_order(node.right)


def main():
    bt = BT()
    bt.add_node(1)
    bt.add_node(3)
    bt.add_node(0)
    bt.add_node(4)

    bt.show()


if __name__ == '__main__':
    main()
