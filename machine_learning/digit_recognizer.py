""" Created by wu.jieyi on 2016/03/31. """
from sklearn.neighbors import KNeighborsClassifier

from machine_learning.kaggle_template import LoadData, Classify, Recognizer


class LoadDataFromCSV(LoadData):
    def _load_train_and_label(self):
        print('loading training data and label data...')
        data_set = super()._load_train_and_label()
        # labels = dataset[:,0]  # La colonna 0 rappresenta le labels
        # data = dataset[:,1:]  # I dati (in unica riga delle immagini)
        return data_set.drop('label', axis=1), data_set['label']

    def _load_test(self):
        print('loading test data...')
        return super()._load_test()


class KnnClassify(Classify):
    """
    K-nearest neighbor.
    """

    @LoadDataFromCSV('train.csv', 'test.csv')
    def classify(self):
        return super(KnnClassify, self).classify()

    def method(self):
        self.classification = KNeighborsClassifier()  # default:k = 5,defined by yourself:KNeighborsClassifier(n_neighbors=10)


def main():
    r = Recognizer()
    r.classify = KnnClassify()
    r.execute()


if __name__ == '__main__':
    main()
