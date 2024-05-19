import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_city_instance_creation(self):
        """Test if a City instance is created properly."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_str_representation(self):
        """Test the string representation of the City instance."""
        city = City()
        self.assertEqual(str(city), f"[City] ({city.id}) {city.to_dict()}")

    def test_to_dict_method(self):
        """Test the to_dict method of the City class."""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)
        self.assertEqual(city_dict["created_at"], city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], city.updated_at.isoformat())

    def test_save_method(self):
        """Test the save method of the City class."""
        city = City()
        old_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(old_updated_at, city.updated_at)

    def test_state_id_attribute(self):
        """Test the state_id attribute of the City class."""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_name_attribute(self):
        """Test the name attribute of the City class."""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
