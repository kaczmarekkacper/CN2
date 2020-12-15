from unittest import TestCase
from Example import Example


class TestExample(TestCase):
    def test_init_values_one_attr(self):
        # Arrange
        example = Example.Example()

        # Act
        example.init_values(["condition", "class"], -1)
        result_attribute = example.attributes
        result_value = example.value

        # Assert
        self.assertEqual(["condition"], result_attribute)
        self.assertEqual("class", result_value)

    def test_init_values_two_attr(self):
        # Arrange
        example = Example.Example()

        # Act
        example.init_values(["condition", "condition2", "class"], -1)
        result_attribute = example.attributes
        result_value = example.value

        # Assert
        self.assertEqual(["condition", "condition2"], result_attribute)
        self.assertEqual("class", result_value)