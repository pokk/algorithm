from abc import ABCMeta, abstractmethod


class DP(metaclass=ABCMeta):
    @abstractmethod
    def _preset(self):
        pass

    @abstractmethod
    def _algorithm(self):
        pass

    @abstractmethod
    def _backtracking(self):
        pass

    @abstractmethod
    def res(self):
        pass
