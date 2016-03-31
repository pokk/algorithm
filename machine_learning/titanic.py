""" Created by wu.jieyi on 2016/03/31. """
from sklearn.ensemble.forest import RandomForestClassifier

from machine_learning.kaggle_template import LoadData, Classify


class LoadDataFromCSV(LoadData):
    def _load_train_and_label(self):
        data_set = super(LoadDataFromCSV, self)._load_train_and_label()

    def _load_test(self):
        pass


class RFClassify(Classify):
    @LoadDataFromCSV('train.csv', 'test.csv')
    def classify(self):
        return super(RFClassify, self).classify()

    def method(self):
        self.classification = RandomForestClassifier()


def main():
    print("hello world")


if __name__ == '__main__':
    main()
