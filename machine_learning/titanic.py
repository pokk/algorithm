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
        self._drop_label = ['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin', 'Embarked', 'SibSp', 'Parch', 'Fare']

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

        return data_set.drop(self._drop_label, axis=1), data_set['Survived']

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

        # Modify the data for loading data.
        drop_data_for_loading = self._drop_label[:]
        drop_data_for_loading.remove('Survived')

        return data_test.drop(drop_data_for_loading, axis=1)

    def _format_result(self, res):
        return OrderedDict(
            zip(self.header, [numpy.array([index for index in range(self.test_passenger_id, self.test_passenger_id + len(res))]), res]))


class RFClassify(Classify):
    def __init__(self):
        super().__init__()

        self.n_estimators = 20
        self.min_samples_leaf = 20
        self.r_random_state = 30

    @LoadDataFromCSV('../train.csv', '../test.csv')
    def classify(self):
        return super(RFClassify, self).classify()

    def method(self):
        self.classification = RandomForestClassifier(n_estimators=4, random_state=30, min_samples_leaf=4, oob_score=False)

    @LoadDataFromCSV('../train.csv', '../test.csv')
    def accuracy(self):
        res = []

        for i in range(1, self.n_estimators):
            for j in range(1, self.min_samples_leaf):
                self.classification = RandomForestClassifier(n_estimators=i, random_state=self.r_random_state, min_samples_leaf=j)
                self._modeling(self.train[:testing_training_number], self.label[:testing_training_number])
                res.append((i, j, self.score(self.train[testing_training_number:], self.label[testing_training_number:])))

        return max(res, key=itemgetter(2))


class TestClassify(Classify):
    def __init__(self):
        super().__init__()

    @LoadDataFromCSV('../train.csv', '../test.csv')
    def classify(self):
        return self.test['Sex'].map({1: 1, 0: 0}).astype(int)

    def method(self):
        pass


def main():
    r = Recognizer()
    r.classify = RFClassify()
    # r.test_accuracy()
    r.execute()

if __name__ == '__main__':
    main()
