import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_user_instance_creation(self):
        """Test if a User instance is created properly."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_str_representation(self):
        """Test the string representation of the User instance."""
        user = User()
        self.assertEqual(
            str(user),
            f"[User] ({user.id}) {user.to_dict()}"
        )

    def test_to_dict_method(self):
        """Test the to_dict method of the User class."""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertEqual(user_dict['created_at'], user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], user.updated_at.isoformat())

    def test_save_method(self):
        """Test the save method of the User class."""
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

    def test_email_attribute(self):
        """Test the email attribute of the User class."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, "")

    def test_password_attribute(self):
        """Test the password attribute of the User class."""
        user = User()
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, "")

    def test_first_name_attribute(self):
        """Test the first_name attribute of the User class."""
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, "")

    def test_last_name_attribute(self):
        """Test the last_name attribute of the User class."""
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
