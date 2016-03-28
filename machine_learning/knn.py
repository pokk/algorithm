""" Created by wu.jieyi on 2016/03/28. """

import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

h = [180, 175, 185, 190, 170, 155, 150, 160, 160, 165]
w = [90, 85, 75, 85, 70, 30, 50, 45, 45, 50]
fig = plt.figure()


def init():
    h_b = np.array(h[:int(len(h) / 2)])
    w_b = np.array(w[:int(len(w) / 2)])

    h_s = np.array(h[int(len(h) / 2):])
    w_s = np.array(w[int(len(w) / 2):])

    plt.scatter(h_b, w_b, c='red', alpha=0.5)  # Draw big person circle.
    plt.scatter(h_s, w_s, c='green', alpha=0.5)  # Draw small person circle.

    plt.xlabel('height')  # x axis label.
    plt.ylabel('weight')  # y axis label.


def knn(n, h_t, w_t):
    dis = []
    for i, j in zip(h, w):
        dis.append(((i - h_t) ** 2 + (j - w_t) ** 2) ** 0.5)

    mini = []
    for i in range(n):
        mini.append(dis.index(min(dis)))
        dis[dis.index(min(dis))] = sys.maxsize

    big, small = 0, 0
    for i in mini:
        if i > len(dis) / 2:
            small += 1
        else:
            big += 1

    return 'big' if big > small else 'small'


init()


# Update the canvas.
def update(i, fig, im):
    res = knn(3, h_r[i], w_r[i])
    p = None

    if res is 'big':
        h.insert(0, h_r[i])
        w.insert(0, w_r[i])
        p = plt.scatter(h_r[i], w_r[i], c='red', alpha=0.5)
    elif res is 'small':
        h.append(h_r[i])
        w.append(w_r[i])
        p = plt.scatter(h_r[i], w_r[i], c='green', alpha=0.5)

    im.append([p])


im = []

h_r = np.random.random_integers(100, 200, 20)  # Random 20 variable between range 100 and 200.
w_r = np.random.random_integers(30, 100, 20)  # Random 20 variable between range 30 and 100.

# Animation for functions.
ani = animation.FuncAnimation(fig, update, fargs=(fig, im), frames=len(h_r), interval=1000, repeat=0)

plt.show()
