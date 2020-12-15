class ConfusionMatrix:
    @staticmethod
    def make_confusion_matrix(set, groups):
        matrix = [['x']]
        for group in groups:
            matrix[0].append(group)
            matrix.append([group])
            for i in range(len(groups)):
                matrix[len(matrix)-1].append(0)
        for example in set:
            column = matrix[0].index(example.value)
            for row in matrix:
                if row[0] == example.prediction:
                    row[column] += 1
        return matrix
