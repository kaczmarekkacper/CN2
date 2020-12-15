class Condition:
    def __init__(self):
        self.attribute_number = None
        self.attribute_value = None

    def is_true(self, example):
        return example.attributes[self.attribute_number] == self.attribute_value
