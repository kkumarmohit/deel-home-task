import unittest
from unittest.mock import patch
from app.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('requests.get')
    def test_reverse_ip(self, mock_get):
        # Mock the response from the external API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"ip": "1.2.19.4"}

        # Expected reversed IP
        expected_reversed_ip = "4.19.2.1"

        # Call the endpoint
        response = self.app.get('/reverse-ip')

        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "original_ip": "1.2.19.4",
            "reversed_ip": expected_reversed_ip
        })

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})

if __name__ == '__main__':
    unittest.main()