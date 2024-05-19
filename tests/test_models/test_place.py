import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_place_instance_creation(self):
        """Test if a Place instance is created properly."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_str_representation(self):
        """Test the string representation of the Place instance."""
        place = Place()
        self.assertEqual(str(place), f"[Place] ({place.id}) {place.to_dict()}")

    def test_to_dict_method(self):
        """Test the to_dict method of the Place class."""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)
        self.assertEqual(place_dict["created_at"],
                         place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"],
                         place.updated_at.isoformat())

    def test_save_method(self):
        """Test the save method of the Place class."""
        place = Place()
        old_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(old_updated_at, place.updated_at)


if __name__ == "__main__":
    unittest.main()
