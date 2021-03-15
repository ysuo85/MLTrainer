import sys
sys.path.append('../Results/')
from abc import abstractmethod
from Results import BaseResults

class BaseClassifierModel:
    def __init__(self):
        self.model = None

    @abstractmethod
    def Train(self, train_x, train_y, val_x, val_y, results: BaseResults, num_epochs=100, learning_rate=0.001, batch_size=64):
        pass

    @abstractmethod
    def Infer(self, test_x, results: BaseResults):
        pass

    @abstractmethod
    def Summarize(self):
        pass