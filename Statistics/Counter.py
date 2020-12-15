class Counter:
    @staticmethod
    def count_predictions(set):
        counter = 0
        for example in set:
            if example.prediction == example.value:
                counter += 1
        return counter