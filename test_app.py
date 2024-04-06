import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode('utf-8'), '¡Hola, mundo!')

if __name__ == '__main__':
    unittest.main()