#!/usr/bin/env python3
"""This Python test class tests the functionality
of a BaseModel class, including attributes like id,
 created_at, and updated_at."""

from models.base_model import BaseModel as bs
from unittest import TestCase as TC
from datetime import datetime as d


class TestEmployee(TC):
    """The `TestEmployee` class contains test methods
    for verifying the functionality of a base class with
    attributes like id, created_at, and updated_at."""

    @classmethod
    def setUpClass(cls):
        """
        The `setUpClass` function initializes instances of a
        class `bs` and creates a dictionary from one of
        the instances to use in creating another instance.

        :param cls: In the code snippet you provided, `cls` i
        s a reference to the class itself. The
        `setUpClass` method is a class method in Python that is
        called before any tests in the test case
        class are run. It is typically used to set up resources
        or configurations that are shared among all
        the
        """
        cls.base1 = bs()
        cls.base2 = bs()
        cls.base3 = bs()
        cls.b3_dict = cls.base3.to_dict()
        cls.base4 = bs(**cls.b3_dict)

    def test_unpacking(self):
        """
        The function `test_unpacking` performs
        assertions related to the `id` attribute of objects
        `base3` and `base4`.
        """
        self.assertEqual(self.base3.id, self.base4.id)
        self.assertIsNotNone(self.base4.id)
        self.assertIsInstance(self.base4.id, str)

    def test_uuid(self):
        """
        The function `test_uuid` checks that the `id`
        attribute of an object is not None, is stored as a
        string, and is unique among different objects.
        """
        self.assertIsNotNone(self.base1.id, "id must not be None")
        self.assertIsInstance(self.base1.id, str,
                              "id must be stored as string")
        self.assertFalse(self.base1.id == self.base2.id, "id must be unique")

    def test_str(self):
        """
        The function `test_str` checks if the `__str__`
        method of an object `base1` returns a string.
        """
        self.assertIsInstance(self.base1.__str__(), str)

    def test_save(self):
        """
        The `test_save` function checks if the `updated_at`
        attribute of an object changes after calling
        the `save` method.
        """
        uptime = self.base1.updated_at
        self.base1.save()
        newuptime = self.base1.updated_at
        self.assertNotEqual(uptime, newuptime)

    def test_createdAt(self):
        """
        The function `test_createdAt` checks if the
        `created_at` attribute of `self.base1` is an
        instance of `d` and is not None.
        """
        self.assertIsInstance(self.base1.created_at, d)
        self.assertIsNotNone(self.base1.created_at)

    def test_updateddAt(self):
        """
        The function `test_updateddAt` checks if the
        `updated_at` attribute of `self.base1` is an instance
        of `d` and is not `None`.
        """
        self.assertIsInstance(self.base1.updated_at, d)
        self.assertIsNotNone(self.base1.updated_at)

    def test_toDict(self):
        """
        The function `test_toDict` checks the output of
        the `to_dict` method for specific data types.
        """
        self.assertIsInstance(self.base1.to_dict(), dict)
        self.assertIsNotNone(self.base1.to_dict())
        self.assertIsInstance(self.base1.to_dict()["created_at"], str)
        self.assertIsInstance(self.base1.to_dict()["updated_at"], str)

    @classmethod
    def tearDownClass(cls):
        """
        The `tearDownClass` function is used in Python to
        clean up resources after a test class has been
        executed.

        :param cls: The `cls` parameter in the `tearDownClass`
        method is a reference to the class
        itself. In this context, it is used to clean up resources
        or perform any necessary teardown
        actions after all the test methods in the class have been
        run. In the provided code snippet, it
        is used to delete
        """
        del cls.base1
        del cls.base2
