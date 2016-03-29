# -*- coding: UTF-8 -*-

import numpy as np
from numpy import ravel
from sklearn.neighbors import KNeighborsClassifier


def knn_classify(train_data, train_label, test_data):
    knn_clf = KNeighborsClassifier(n_neighbors=2)  # default:k = 5,defined by yourself:KNeighborsClassifier(n_neighbors=10)
    knn_clf.fit(train_data, ravel(train_label))
    test_label = knn_clf.predict(test_data)
    return test_label


h = [180, 175, 160, 165, 185, 190, 170, 155, 150, 160]  # Height
w = [90, 85, 45, 50, 75, 85, 70, 30, 50, 45]  # Weight
l = np.array(['big', 'big', 'small', 'small', 'big', 'big', 'big', 'small', 'small', 'small'])  # Label of result.
t = np.array([])

# Combine the h and w.
for i, j in zip(h, w):
    t = np.concatenate((t, np.array([i, j])), axis=0)
# Re-shape to 2 dimension.
t.shape = -1, 2

# Test data.
f = np.array([190, 100,
              140, 30,
              100, 20,
              160, 60])
f.shape = -1, 2

t_l = knn_classify(t, l, f)
print(t_l)
