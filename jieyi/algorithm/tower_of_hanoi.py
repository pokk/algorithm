""" Created by wu.jieyi on 2016/02/24. """


class TowerOfHanoi:
    def __init__(self):
        self._tower_flow = []
        pass

    def recursive_hanoi(self, t_a, t_b, t_c, dish):
        """ Algorithm
        1. Move dish of number of n - 1 from tower A to tower B.
        2. Move the biggest one dish from tower A to tower C.
        3. Move dish of number of n - 1 from tower B to tower C.

        :param t_a: Tower A.
        :param t_b: Tower B.
        :param t_c: Tower C.
        :param dish: The number of dish.
        """

        if dish is 0:
            return

        self.recursive_hanoi(t_a, t_c, t_b, dish - 1)
        self._tower_flow.append((str(dish), t_a, t_c))
        self.recursive_hanoi(t_b, t_a, t_c, dish - 1)

    @property
    def tower_flow(self):
        return self._tower_flow


def main():
    c = TowerOfHanoi()
    c.recursive_hanoi('A', 'B', 'C', 3)

    for move in c.tower_flow:
        print("dish:%s from tower %s to tower %s" % move)
    print('total step:', len(c.tower_flow))


if __name__ == '__main__':
    main()
