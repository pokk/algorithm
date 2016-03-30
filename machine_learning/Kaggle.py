""" Created by Jieyi on 3/30/16. """

from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from functools import wraps

import numpy
import pandas
from numpy import ravel
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


class LoadData:
    def __init__(self, train_file_name, test_file_name):
        self.train_filename = train_file_name
        self.test_filename = test_file_name
        self.header = ['ImageId', 'Label']

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            decoratee = args[0]
            decoratee.train, decoratee.label = self.load_train_and_label()
            decoratee.test = self.load_test()

            print('calculating....')
            res = func(*args, **kwargs)
            print('finish calculating...')

            print('saving results into file...')
            self.save_result(self._format_result(res), ''.join([decoratee.__class__.__name__, '.csv']))
            return res

        return wrapper

    def load_train_and_label(self):
        print('loading training data and label data...')
        data_set = pandas.read_csv(self.train_filename)
        # labels = dataset[:,0]  # La colonna 0 rappresenta le labels
        # data = dataset[:,1:]  # I dati (in unica riga delle immagini)
        return data_set.drop('label', axis=1)[:100], data_set['label'][:100]

    def load_test(self):
        print('loading test data...')
        df_test = pandas.read_csv(self.test_filename)
        return df_test[:100]

    def _format_result(self, res):
        return OrderedDict(zip(self.header, [numpy.array([index for index in range(1, len(res) + 1)]), res]))

    def save_result(self, result, file_name):
        pandas.DataFrame(result).to_csv(file_name, encoding='utf-8', header=self.header, index=False)


class Classify(metaclass=ABCMeta):
    def __init__(self):
        self.train = None
        self.label = None
        self.test = None

    @abstractmethod
    def classify(self):
        pass


class KnnClassify(Classify):
    """
    K-nearest neighbor.
    """

    @LoadData('train.csv', 'test.csv')
    def classify(self):
        knn_clf = KNeighborsClassifier()  # default:k = 5,defined by yourself:KNeighborsClassifier(n_neighbors=10)
        knn_clf.fit(self.train, ravel(self.label))
        test_label = knn_clf.predict(self.test)

        return test_label


class RandomForest(Classify):
    @LoadData('train.csv', 'test.csv')
    def classify(self):
        rf_clf = RandomForestClassifier()
        rf_clf.fit(self.train, ravel(self.label))
        test_label = rf_clf.predict(self.test)

        return test_label


class Recognizer:
    def __init__(self, strategy=None):
        self._classify_strategy = strategy

    def execute(self):
        self._classify_strategy.classify()

    @property
    def classify(self):
        return self._classify_strategy

    @classify.setter
    def classify(self, value):
        self._classify_strategy = value


def main():
    r = Recognizer()
    r.classify = KnnClassify()
    r.execute()


if __name__ == '__main__':
    main()
