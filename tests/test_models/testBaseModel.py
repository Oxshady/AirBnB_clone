#!/usr/bin/env python3
from unittest import TestCase as TC, main as m
from models.base_model import BaseModel as BS
class TestEmployee(TC):
    def setUp(self) -> None:
        self.base1 = BS()
        self.base2 = BS()
    def test_uuid(self):
        self.assertIsNotNone(self.base1.id, "id must not be None")
        self.assertIsInstance(self.base1.id, str, "id must be stored as string")
        self.assertFalse(self.base1.id == self.base2.id, "id must be unique")
if __name__ == "__main__":
    m()