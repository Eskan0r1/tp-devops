import unittest
from unittest.mock import patch, MagicMock
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch("app.redis.Redis")  # Mock Redis
    def test_home(self, mock_redis_class):
        # Crée un mock de Redis
        mock_redis_instance = MagicMock()
        mock_redis_instance.exists.return_value = True
        mock_redis_instance.get.return_value = b"1"
        mock_redis_class.return_value = mock_redis_instance

        response = self.app.get('/')
        self.assertIn("Visites :", response.data.decode())  # Vérifie que "Visites :" est dans la réponse

if __name__ == "__main__":
    unittest.main()
