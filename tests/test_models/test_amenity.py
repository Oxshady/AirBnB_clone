import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Review class."""

    def test_review_instance_creation(self):
        """Test if a Review instance is created properly."""
        aminety = Amenity()
        self.assertIsInstance(aminety, Amenity)
        self.assertTrue(hasattr(aminety, "id"))
        self.assertTrue(hasattr(aminety, "created_at"))
        self.assertTrue(hasattr(aminety, "updated_at"))
