class Example:
    def __init__(self):
        self.value = None
        self.attributes = []
        self.prediction = None

    def init_values(self, row, prediction_position):
        self.value = row.pop(prediction_position)
        self.attributes = row
