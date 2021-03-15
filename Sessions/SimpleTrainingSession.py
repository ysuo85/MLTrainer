import sys
sys.path.append('../Results')
sys.path.append('../Models')
from Models import BaseClassifierModel
from Results import BaseResults
from Sessions import BaseSession

class SimpleTrainingSession(BaseSession):
    def __init__(self, model):
        super().__init__(self)
        self.model = model
        self.results = Results.BaseResults()

    def onTrainingComplete(self):
        print("SimpleTrainingSession::onTrainingComplete called")

    def onTrainingFailed(self):
        print("SimpleTrainingSession::onTrainingFailed called")

    def onTrainingPaused(self):
        print("SimpleTrainingSession::onTrainingPaused called")

    def Start(self):
        print("SimpleTrainingSession::Start called")

    def GetSessionOutcome(self):
        print("SimpleTrainingSession::GetSessionOutcome called")
        return (self.model, self.results)