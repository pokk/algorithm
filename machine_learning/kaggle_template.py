""" Created by Jieyi on 3/30/16. """

from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from functools import wraps

import numpy
import pandas
from numpy import ravel


class LoadData:
    """
    Decorator of loading the training data and testing data.
    """

    def __init__(self, train_file_name, test_file_name):
        self.train_filename = train_file_name
        self.test_filename = test_file_name
        self.header = ['ImageId', 'Label']

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            decoratee = args[0]
            decoratee.train, decoratee.label = self._load_train_and_label()
            decoratee.test = self._load_test()

            print('calculating....')
            res = func(*args, **kwargs)
            print('finish calculating...')

            print('saving results into file...')
            self._save_result(self._format_result(res), ''.join([decoratee.__class__.__name__, '.csv']))
            return res

        return wrapper

    @abstractmethod
    def _load_train_and_label(self):
        """
        You have to return two variable.

        The first: It will be training data without labels.
        The second: It will be training data's labels.
        """

        return pandas.read_csv(self.train_filename)

    @abstractmethod
    def _load_test(self):
        return pandas.read_csv(self.test_filename)

    def _save_result(self, result, file_name):
        pandas.DataFrame(result).to_csv(file_name, encoding='utf-8', header=self.header, index=False)

    def _format_result(self, res):
        return OrderedDict(zip(self.header, [numpy.array([index for index in range(1, len(res) + 1)]), res]))


class Classify(metaclass=ABCMeta):
    """
    Classification's category prototype.
    """

    def __init__(self):
        self.train = None
        self.label = None
        self.test = None
        self.classification = None

    def __new__(cls, *args, **kwargs):
        # if cls.__dict__.get('classify'):
        #     raise SyntaxError('Overriding classify is not allowed')
        return super().__new__(cls, *args, **kwargs)

    @abstractmethod
    def method(self):
        pass

    @abstractmethod
    def classify(self):
        """
        Just using your decorator to this method.
        The context is just 'return super(KnnClassify, self).classify()'.
        """

        self.method()
        self._modeling(self.train, self.label)
        return self._predict()

    def score(self, known_data, known_label):
        return self.classification.score(known_data, known_label)

    def _predict(self):
        print('predicting...')
        return self.classification.predict(self.test)

    def _modeling(self, train_data, train_label):
        print('modeling...')
        self.classification.fit(train_data, ravel(train_label))


class Recognizer:
    """
    Classification's invoker.
    """

    def __init__(self, strategy=None):
        self._classify_strategy = strategy

    def execute(self):
        print(self._classify_strategy.classify())

    @property
    def classify(self):
        return self._classify_strategy

    @classify.setter
    def classify(self, value):
        self._classify_strategy = value


def main():
    pass


if __name__ == '__main__':
    main()
