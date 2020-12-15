from Condition import Condition
import math


class Rule:
    def __init__(self):
        self.conditions = []
        self.prediction = None
        self.entropy = None
        self.significance = None
        self.examples_covered = []
        self.values_probability = None
        self.default_prediction = None

    def add_existing_conditions(self, conditions):
        self.conditions += conditions

    def eval(self, example):
        if self.default_prediction:
            return self.default_prediction
        if self.meets_conditions(example):
            return self.prediction
        else:
            return None

    def add_condition(self, attr_number, attr_value):
        con = Condition.Condition()
        con.attribute_number = attr_number
        con.attribute_value = attr_value
        self.conditions.append(con)

    def meets_conditions(self, example):
        for condition in self.conditions:
            if not condition.is_true(example):
                return False
        return True

    def fill_examples_covered(self, train_set):
        for example in train_set:
            if self.meets_conditions(example):
                self.examples_covered.append(example)

    def calculate_scores(self, whole_train_set_prob):
        self.__calculate_prediction_probabilities()
        self.__calculate_entropy()
        self.__calculate_significance(whole_train_set_prob)

    def __calculate_prediction_probabilities(self):
        values = self.__get_dict_of_values()
        size_of_examples_covered = len(self.examples_covered)
        probability_of_values = {}
        for value in values:
            probability_of_values[value] = (values[value] / size_of_examples_covered)
        self.values_probability = probability_of_values

    def __calculate_entropy(self):
        entropy = 0
        for value in self.values_probability:
            entropy += self.__calculate_single_entropy(self.values_probability[value])
        self.entropy = entropy

    def __get_dict_of_values(self):
        values = {}
        for example in self.examples_covered:
            if example.value in values.keys():
                values[example.value] += 1
            else:
                values[example.value] = 1
        return values

    @staticmethod
    def __calculate_single_entropy(probability):
        log2_of_prob = math.log(probability, 2)
        entropy = -1*probability*log2_of_prob
        return entropy

    def __calculate_significance(self, whole_train_set_prob):
        significance = 0
        for value in self.values_probability:
            significance += self.__calculate_single_significance(self.values_probability[value],
                                                               whole_train_set_prob[value])
        self.significance = 2*significance

    @staticmethod
    def __calculate_single_significance(covered_prob, whole_prob):
        significance = covered_prob * math.log(covered_prob/whole_prob, 10)
        return significance

    def check_if_conditions_unique(self):
        last_condition = self.__get_last_condition()
        for condition in self.conditions:
            if last_condition == condition:
                continue
            if condition.attribute_number == last_condition.attribute_number:
                if condition.attribute_value == last_condition.attribute_value:
                    return False
        return True

    def __get_last_condition(self):
        return self.conditions[len(self.conditions)-1]
