import unittest
from unittest.mock import patch
from app.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_reverse_ip_with_x_forwarded_for(self):
        # Simulate a request with the X-Forwarded-For header
        headers = {'X-Forwarded-For': '203.0.113.42:12345'}
        response = self.app.get('/reverse-ip', headers=headers)

        # Expected reversed IP
        expected_reversed_ip = "42.113.0.203"

        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "original_ip": "203.0.113.42",
            "reversed_ip": expected_reversed_ip
        })

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})

if __name__ == '__main__':
    unittest.main()