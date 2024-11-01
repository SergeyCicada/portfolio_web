import pytest
from flask_testing import TestCase
from portfolio_web.run import app

class TestConfig(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'I am seeking an opportunity to join', response.data)

if __name__ == '__main__':
    pytest.main()