#!/usr/bin/python3
"""
Unit tests for the State class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up test environment.
        This method is called before each test.
        """
        self.state = State()

    def test_instance(self):
        """
        Test if the object is an instance of State.
        """
        self.assertIsInstance(self.state, State)

    def test_inheritance(self):
        """
        Test if State inherits from BaseModel.
        """
        from models.base_model import BaseModel

        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attributes(self):
        """
        Test default value of the name attribute.
        """
        self.assertEqual(self.state.name, "")

    def test_attribute_assignment(self):
        """
        Test assigning a value to the name attribute.
        """
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_to_dict(self):
        """
        Test to_dict method to ensure it includes State attributes.
        """
        self.state.name = "California"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["name"], "California")
        self.assertIn("name", state_dict)

    def test_str(self):
        """
        Test the string representation of the State instance.
        """
        string = str(self.state)
        self.assertIn("[State]", string)
        self.assertIn(f"({self.state.id})", string)


if __name__ == "_main_":
    unittest.main()
