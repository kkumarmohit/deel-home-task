import unittest
from app.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_reverse_ip(self):
        # Simulate a request with a specific IP address
        test_ip = "1.2.19.4"
        expected_reversed_ip = "4.19.2.1"
        response = self.app.get('/reverse-ip', environ_base={'REMOTE_ADDR': test_ip})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "original_ip": test_ip,
            "reversed_ip": expected_reversed_ip
        })

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "healthy"})

if __name__ == '__main__':
    unittest.main()