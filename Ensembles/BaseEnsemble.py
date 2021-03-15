from abc import abstractmethod

class BaseEnsemble:
    def __init__(self, models=None):
        if models is not None:
            self.models = models
        else:
            self.models = []
    
    def AddModel(self, model):
        self.models.append(model)

    @abstractmethod
    def Infer(self, test_x):
        pass