class BaseResults:
    def __init__(self):
        self.confusion_matrix = []
        self.train_accuracy = 0.0
        self.val_accuracy = 0.0
        self.test_accuracy = 0.0
        self.inference_time_ns = 0