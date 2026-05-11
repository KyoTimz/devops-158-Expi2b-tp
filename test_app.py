import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_response_contains_hello(self):
        response = self.app.get('/')
        self.assertIn('Hello', response.data.decode('utf-8'))

    def test_response_not_empty(self):
        response = self.app.get('/')
        self.assertTrue(len(response.data) > 0)

    def test_response_type_is_string(self):
        response = self.app.get('/')
        self.assertIsInstance(response.data.decode('utf-8'), str)

if __name__ == '__main__':
    unittest.main()
