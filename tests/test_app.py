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

    def test_get_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'- Programming Language: Python', response.data)

    def test_get_contacts(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b' I am ready to provide additional information', response.data)

    def test_get_thank(self):
        response = self.client.get('/thank/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you for your', response.data)

if __name__ == '__main__':
    pytest.main()