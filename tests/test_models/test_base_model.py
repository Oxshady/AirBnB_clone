#!/usr/bin/env python3
"""This Python test class tests the functionality
of a BaseModel class, including attributes like id,
 created_at, and updated_at."""

from models.base_model import BaseModel
from unittest import TestCase
from datetime import datetime


class TestBaseModel(TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.model = BaseModel()

    def test_id_is_unique(self):
        """Test that the id is unique"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method_updates_updated_at(self):
        """Test that save method updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains the correct keys"""
        model_dict = self.model.to_dict()
        expected_keys = ["id", "created_at", "updated_at", "__class__"]
        for key in expected_keys:
            self.assertIn(key, model_dict)

    def test_to_dict_values(self):
        """Test that to_dict returns correct values"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())

    def test_str_method(self):
        """Test the __str__ method"""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.to_dict()}"
        self.assertEqual(str(self.model), expected_str)

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        data = {
            "id": "123",
            "created_at": "2023-05-19T15:22:34.123456",
            "updated_at": "2023-05-19T15:22:34.123456",
            "__class__": "BaseModel",
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, "123")
        self.assertEqual(
            model.created_at,
            datetime.fromisoformat("2023-05-19T15:22:34.123456")
        )
        self.assertEqual(
            model.updated_at,
            datetime.fromisoformat("2023-05-19T15:22:34.123456")
        )
