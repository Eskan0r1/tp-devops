import unittest
from unittest.mock import patch, MagicMock
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch("app.redis.Redis")  # Mock Redis pour le test
    def test_home(self, mock_redis):
        mock_instance = MagicMock()
        mock_instance.exists.return_value = True
        mock_instance.get.return_value = b"1"
        mock_instance.incr.return_value = 2
        mock_redis.return_value = mock_instance

        response = self.app.get('/')
        self.assertIn("Visites :", response.data.decode())

    def test_hello(self):
        response = self.app.get('/hello')
        self.assertEqual(response.data.decode(), "Hello DevOps")

if __name__ == "__main__":
    unittest.main()
