""" Created by Jieyi on 2/11/16. """
from collections import OrderedDict


class TriesNode:
    def __init__(self):
        self.node = OrderedDict.fromkeys([chr(c) for c in range(ord('a'), ord('z') + 1)], None)

    def __str__(self):
        res = {}
        for k, v in self.node.items():
            if v is not None:
                res.update({k: v})
        return str(res)


class Tries:
    def __init__(self):
        self._head = None

    def add(self, word):
        """
        Each character of the word put into the tree as following each character.

        :param word: For adding into the tries.
        """

        def inner_add(node, inner_word, index=0):
            if index is len(inner_word):
                return

            if node.node.get(inner_word[index]) is None:
                node.node[inner_word[index]] = TriesNode()
            inner_add(node.node.get(inner_word[index]), inner_word, index + 1)

        if not self._head:
            self._head = TriesNode()
        inner_add(self._head, word)

    def show(self):
        def travel(key, node):
            tmp = {}
            for k, v in node.node.items():
                if v is not None:
                    tmp.update({k: v})

            print(key)
            for k, ptr in tmp.items():
                travel(k, ptr)

        travel(None, self._head)
        pass


def main():
    words = ['Hello', 'my', 'name', 'is', 'Jieyi', 'I', 'am', 'living', 'in', 'Taiwan',
             'Happy', 'to', 'see', 'you']

    t = Tries()
    for word in words:
        t.add(word.lower())
    t.show()


if __name__ == '__main__':
    main()
