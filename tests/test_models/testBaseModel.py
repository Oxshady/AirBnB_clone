#!/usr/bin/env python3
from models.base_model import BaseModel as bs
from unittest import TestCase as TC
from datetime import datetime as d
class TestEmployee(TC):
    def setUp(self) -> None:
        self.base1 = bs()
        self.base2 = bs()
    def test_uuid(self):
        self.assertIsNotNone(self.base1.id, "id must not be None")
        self.assertIsInstance(self.base1.id, str, "id must be stored as string")
        self.assertFalse(self.base1.id == self.base2.id, "id must be unique")
    def test_str(self):
        self.assertEqual(self.base1.__str__(), f"[{self.base1.__class__.__name__}] ({self.base1.id}) {self.base1.__dict__}")
        self.assertIsInstance(self.base1.__str__(),str)
    def test_save(self):
        uptime = self.base1.updated_at
        self.base1.save()
        newuptime = self.base1.updated_at
        self.assertNotEqual(uptime, newuptime)
    def test_createdAt(self):
        self.assertIsInstance(self.base1.created_at, d)
        self.assertIsNotNone(self.base1.created_at)
    def test_createdAt(self):
        self.assertIsInstance(self.base1.updated_at, d)
        self.assertIsNotNone(self.base1.updated_at)
    def test_toDict(self):
        self.assertIsInstance(self.base1.to_dict(), dict)
        self.assertIsNotNone(self.base1.to_dict())
        self.assertIsInstance(self.base1.to_dict()["created_at"], str)
        self.assertIsInstance(self.base1.to_dict()["updated_at"], str)
        
        