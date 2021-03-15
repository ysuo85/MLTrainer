import sys
sys.path.append('../Results/')
from Results import BaseResults
from Models import BaseClassifierModel

class Vgg16KerasModel(BaseClassifierModel):
    def __init__(self):
        super().__init__(self)

    def Train(self, train_x, train_y, val_x, val_y, results: BaseResults, num_epochs=100, learning_rate=0.001, batch_size=64):
        print("Vgg16KerasModel::Train called")

    def Infer(self, test_x, results: BaseResults):
        print("Vgg16KerasModel::Infer called")

    def Summarize(self):
        print("Vgg16KerasModel::Summarize called")