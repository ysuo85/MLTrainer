import sys
from Ensembles import BaseEnsemble

class SimpleAveragingEnsemble(BaseEnsemble):
    def __init__(self):
        super().__init__(self)

    def Infer(self, test_x):
        print("SimpleAveragingEnsemble::Infer called")