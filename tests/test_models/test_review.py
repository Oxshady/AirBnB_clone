import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_review_instance_creation(self):
        """Test if a Review instance is created properly."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_str_representation(self):
        """Test the string representation of the Review instance."""
        review = Review()
        self.assertEqual(
            str(review),
            f"[Review] ({review.id}) {review.to_dict()}"
        )

    def test_to_dict_method(self):
        """Test the to_dict method of the Review class."""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)
        self.assertEqual(review_dict['created_at'], review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'], review.updated_at.isoformat())

    def test_save_method(self):
        """Test the save method of the Review class."""
        review = Review()
        old_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(old_updated_at, review.updated_at)


if __name__ == '__main__':
    unittest.main()
