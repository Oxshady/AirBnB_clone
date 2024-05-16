#!/usr/bin/env python3
from models.base_model import BaseModel as bs
from unittest import TestCase as TC
from datetime import datetime as d


class TestEmployee(TC):
    @classmethod
    def setUpClass(cls):
        cls.base1 = bs()
        cls.base2 = bs()
        cls.base3 = bs()
        cls.b3_dict = cls.base3.to_dict()
        cls.base4 = bs(**cls.b3_dict)
    
    def test_unpacking(self):
        self.assertEqual(self.base3.id, self.base4.id)
        self.assertIsNotNone(self.base4.id)
        self.assertIsInstance(self.base4.id,str)
    def test_uuid(self):
        self.assertIsNotNone(self.base1.id, "id must not be None")
        self.assertIsInstance(self.base1.id, str,
                              "id must be stored as string")
        self.assertFalse(self.base1.id == self.base2.id, "id must be unique")

    def test_str(self):
        self.assertIsInstance(self.base1.__str__(), str)

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

    @classmethod
    def tearDownClass(cls):
        del cls.base1
        del cls.base2
