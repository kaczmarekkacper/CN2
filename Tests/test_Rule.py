from unittest import TestCase
from Example import Example
from Rule import Rule
from Condition import Condition


class TestRule(TestCase):
    def test_add_existing_conditions_one(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "class"], -1)

        rule = Rule.Rule()

        condition = Condition.Condition()
        condition.attribute_number = 0
        condition.attribute_value = "condition"

        # Act
        rule.add_existing_conditions([condition])

        # Assert
        self.assertTrue(rule.meets_conditions(example))

    def test_add_existing_conditions_two(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "condition2", "class"], -1)

        rule = Rule.Rule()

        condition = Condition.Condition()
        condition.attribute_number = 0
        condition.attribute_value = "condition"

        condition2 = Condition.Condition()
        condition2.attribute_number = 1
        condition2.attribute_value = "condition2"

        list_of_con = [condition, condition2]

        # Act
        rule.add_existing_conditions(list_of_con)
        # Assert
        self.assertTrue(rule.meets_conditions(example))

    def test_eval_test_default_rule(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "condition2", "class"], -1)

        rule = Rule.Rule()

        condition = Condition.Condition()
        condition.attribute_number = 0
        condition.attribute_value = "condition"

        condition2 = Condition.Condition()
        condition2.attribute_number = 1
        condition2.attribute_value = "condition2"

        list_of_con = [condition, condition2]

        # Act
        rule.add_existing_conditions(list_of_con)
        # Assert
        self.assertTrue(rule.meets_conditions(example))

    def test_add_condition_one(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "class"], -1)

        rule = Rule.Rule()
        # Act
        rule.add_condition(0, "condition")

        # Assert
        self.assertTrue(rule.meets_conditions(example))

    def test_add_condition_two(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "condition2", "class"], -1)

        rule = Rule.Rule()
        # Act
        rule.add_condition(0, "condition")
        rule.add_condition(1, "condition2")

        # Assert
        self.assertTrue(rule.meets_conditions(example))

    def test_meets_conditions_one_true(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "class"], -1)

        rule = Rule.Rule()
        # Act
        rule.add_condition(0, "condition")

        # Assert
        self.assertTrue(rule.meets_conditions(example))

    def test_meets_conditions_two_true(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "condition2", "class"], -1)

        rule = Rule.Rule()
        # Act
        rule.add_condition(0, "condition")
        rule.add_condition(1, "condition2")

        # Assert
        self.assertTrue(rule.meets_conditions(example))

    def test_meets_conditions_two_false_first_false(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "condition2", "class"], -1)

        rule = Rule.Rule()
        # Act
        rule.add_condition(0, "condition")
        rule.add_condition(1, "condition3")

        # Assert
        self.assertFalse(rule.meets_conditions(example))

    def test_meets_conditions_two_false_second_false(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "condition2", "class"], -1)

        rule = Rule.Rule()
        # Act
        rule.add_condition(0, "condition1")
        rule.add_condition(1, "condition2")

        # Assert
        self.assertFalse(rule.meets_conditions(example))

    def test_fill_examples_covered(self):
        self.assertTrue(True)

    def test_calculate_scores(self):
        self.assertTrue(True)

    def test_check_if_conditions_unique(self):
        self.assertTrue(True)
