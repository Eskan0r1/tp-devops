import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertIn("Visites :", response.data.decode())

if __name__ == "__main__":
    unittest.main()
