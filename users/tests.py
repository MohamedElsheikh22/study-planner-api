from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.

class AuthTest(APITestCase):
    def test_register(self):
        data = {
            'username': 'testuser',
            'email': 'test@test.com',
            'password': 'testpass123'
        }
        response = self.client.post('/api/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        self.client.post('/api/auth/register/', {
            'username': 'Mohamed',
            'email': 'm@email.com',
            'password': '123456'
        })
        response = self.client.post('/api/auth/login/', {
            'username': 'Mohamed',
            'password': '123456'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
