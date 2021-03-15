from abc import abstractmethod
class BaseSession(object):
    def __init__(self):
        self.print_epochs = True
        self.print_accuracy = True
        self.print_model = True
        self.human_in_the_loop = False

    @abstractmethod
    def onTrainingComplete(self):
        pass

    @abstractmethod
    def onTrainingFailed(self):
        pass

    @abstractmethod
    def onTrainingPaused(self):
        pass

    @abstractmethod
    def Start(self):
        pass

    @abstractmethod
    def GetSessionOutcome(self):
        pass