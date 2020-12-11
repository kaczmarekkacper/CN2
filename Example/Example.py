

class Example:
    def __init__(self):
        self.value = -1
        self.attributes = []
        self.prediction = -1

    def init_values(self, row, prediction_position):
        self.value = row.pop(prediction_position)
        self.attributes = row