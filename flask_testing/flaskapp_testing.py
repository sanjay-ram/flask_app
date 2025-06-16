from flask_testing import TestCase
import unittest
from flask_project import app

class FlaskTesting(TestCase):
    def create_app(self):
        return app
    def test_index(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertEqual(response.data, b'Hello Flask!')


if __name__ == '__main__':
    unittest.main()