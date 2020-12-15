from unittest import TestCase
from Example import Example
from Condition import Condition


class TestCondition(TestCase):
    def test_is_true_return_true(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "class"], -1)

        condition = Condition.Condition()
        condition.attribute_number = 0
        condition.attribute_value = "condition"

        # Act
        result = condition.is_true(example)

        # Assert
        self.assertTrue(result)

    def test_is_true_return_false(self):
        # Arrange
        example = Example.Example()
        example.init_values(["condition", "class"], -1)

        condition = Condition.Condition()
        condition.attribute_number = 0
        condition.attribute_value = "not_condition"

        # Act
        result = condition.is_true(example)

        # Assert
        self.assertFalse(result)
