import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.id = "1234"
        FileStorage._FileStorage__objects = {}
        self.storage.new(self.base_model)

    def tearDown(self):
        """Clean up after the tests"""
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Test the all method"""
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn("BaseModel.1234", all_objects)

    def test_new_method(self):
        """Test the new method"""
        new_model = BaseModel()
        new_model.id = "5678"
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn("BaseModel.5678", all_objects)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_method(self, mock_file):
        """Test the save method"""
        self.storage.save()
        mock_file.assert_called_once_with("file.json", "w")

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='{"BaseModel.1234": {"__class__": "BaseModel", "id": "1234", "created_at": "2023-05-19T15:22:34.123456", "updated_at": "2023-05-19T15:22:34.123456"}}',
    )
    @patch("os.path.exists", return_value=True)
    def test_reload_method(self, mock_exists, mock_file):
        """Test the reload method"""
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn("BaseModel.1234", all_objects)
        self.assertEqual(all_objects["BaseModel.1234"].id, "1234")


if __name__ == "__main__":
    unittest.main()
