""" Created by wu.jieyi on 2016/03/31. """
from _operator import itemgetter
from collections import OrderedDict

import numpy
from sklearn.ensemble.forest import RandomForestClassifier

from machine_learning import testing_training_number
from machine_learning.kaggle_template import LoadData, Classify, Recognizer


class LoadDataFromCSV(LoadData):
    def __init__(self, train_file_name, test_file_name):
        super().__init__(train_file_name, test_file_name)
        self.header = ['PassengerId', 'Survived']
        self.test_passenger_id = 0

    def _load_train_and_label(self):
        data_set = super()._load_train_and_label()
        # 'pclass', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked'
        # We don't consider 'name', 'ticket', 'cabin', 'embarked'.
        # We have to consider 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare'
        ms_list = ['Lady', 'the Countess', 'Mlle', 'Mee', 'Ms']
        mr_list = ['Capt', 'Don', 'Major', 'Sir', 'Col', 'Jonkheer', 'Rev', 'Dr', 'Master']
        mrs_list = ['Dona']

        # Modify the data.
        # Modify sex from string to int.
        data_set['Sex'] = data_set['Sex'].map({'female': 1, 'male': 0}).astype(int)
        # Modify age from float to int.
        data_set.Age.fillna(data_set.Age.median(), inplace=True)
        data_set.Age = data_set.Age.astype(int)

        data_set.Name = data_set.Name.str.replace('|'.join(ms_list), 'Miss')
        data_set.Name = data_set.Name.str.replace('|'.join(mr_list), 'Mr')
        data_set.Name = data_set.Name.str.replace('|'.join(mrs_list), 'Mrs')

        return data_set.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis=1), data_set['Survived']

    def _load_test(self):
        data_test = super()._load_test()

        # Modify the data.
        # Modify sex from string to int.
        data_test['Sex'] = data_test['Sex'].map({'female': 1, 'male': 0}).astype(int)
        # Modify age from float to int.
        data_test.Age.fillna(data_test.Age.median(), inplace=True)
        data_test.Age = data_test.Age.astype(int)

        data_test.Fare.fillna(data_test.Fare.median(), inplace=True)

        self.test_passenger_id = data_test.PassengerId.iloc[0]

        return data_test.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

    def _format_result(self, res):
        return OrderedDict(
            zip(self.header, [numpy.array([index for index in range(self.test_passenger_id, self.test_passenger_id + len(res))]), res]))


class RFClassify(Classify):
    @LoadDataFromCSV('../train.csv', '../test.csv')
    def classify(self):
        return super(RFClassify, self).classify()

    def method(self):
        self.classification = RandomForestClassifier(n_estimators=14, random_state=30, min_samples_leaf=3, oob_score=True)

    @LoadDataFromCSV('../train.csv', '../test.csv')
    def accuracy(self):
        n_estimators = 100
        min_samples_leaf = 300
        res = []

        for i in range(1, n_estimators):
            for j in range(1, min_samples_leaf):
                self.classification = RandomForestClassifier(n_estimators=i, random_state=30, min_samples_leaf=j)
                self._modeling(self.train[:testing_training_number], self.label[:testing_training_number])
                res.append((i, j, self.score(self.train[testing_training_number:], self.label[testing_training_number:])))

        return max(res, key=itemgetter(2))


def main():
    r = Recognizer()
    r.classify = RFClassify()
    r.execute()


if __name__ == '__main__':
    main()
