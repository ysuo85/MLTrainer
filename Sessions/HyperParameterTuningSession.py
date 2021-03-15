import sys
sys.path.append('../Results')
sys.path.append('../Models')
from Results import BaseResults
from Models import BaseClassifierModel
from Sessions import BaseSession

class HyperParameterTuningSession(BaseSession):
    def __init__(self, tuner, model):
        super().__init__(self)
        self.tuner = tuner
        self.tuned_models = []
        self.best_model = None
        self.tuned_results = []
        self.best_result = None

    def onTrainingComplete(self):
        print("HyperParameterTuningSession::onTrainingComplete called")

    def onTrainingFailed(self):
        print("HyperParameterTuningSession::onTrainingFailed called")

    def onTrainingPaused(self):
        print("HyperParameterTuningSession::onTrainingPaused called")

    def Start(self):
        print("HyperParameterTuningSession::Start called")

    def GetSessionOutcome(self):
        print("HyperParameterTuningSession::GetSessionOutcome called")
        return (self.best_model, self.best_results)