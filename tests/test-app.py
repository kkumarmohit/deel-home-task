import unittest
from app.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_reverse_ip(self):
        response = self.app.get('/reverse-ip')
        self.assertEqual(response.status_code, 200)

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "healthy"})

if __name__ == '__main__':
    unittest.main()