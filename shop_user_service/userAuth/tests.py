import pytest
from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from userAuth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from allauth.account.models import EmailAddress

class UserAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url_register = reverse('rest_register')
        self.url_login = reverse('rest_login')
        self.url_logout = reverse('rest_logout')

        self.user = {
            'username': 'rickdeu',
            'email': '<your_email>',
            'password1': '<your_password>',
            'password2': '<your_password>',
            'status':'Active',
            'gender':'<M/F>',
            'first_name':'<your_first_name>',
            'last_name':'<your_last_name>',
            'phone_number':'<your_phone_number>'
        }

    def _create_test_image(self):
        image = Image.new('RGB', (100, 100))
        image_file = BytesIO()
        image.save(image_file, 'png')
        image_file.seek(0)
        return SimpleUploadedFile('test.png', image_file.read(), content_type='image/png')

    def test_post_and_get_registration(self):
        """Ensure we can create and retrieve a user"""
        response = self.client.post(
            self.url_register, self.user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_login(self):
        """Ensure we can create a login"""
        response = self.client.post(
            self.url_register, self.user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
     
        verified_emails = EmailAddress.objects.get(email=self.user['email'])
        verified_emails.verified=True
        verified_emails.save()
        credentials = {
            'username': self.user['username'],
            'email': self.user['email'],
            'password': self.user['password1'],
        }
        response = self.client.post(self.url_login, credentials, format='json')
        
        print('Response user login: ', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
    
    def test_post_login_no_verified_mail(self):
        """Ensure we can create a login"""
        response = self.client.post(
            self.url_register, self.user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        credentials = {
            'username': '<your_username>',
            'email': '<your_email>',
            'password': '<your_password>',
        }

        response = self.client.post(self.url_login, credentials, format='json')
        print('Response user login: ', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_logout(self):
        """Ensure we can logout"""
        response = self.client.post(
            self.url_register, self.user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.url_logout, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
