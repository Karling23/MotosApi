from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from motostore.tests.helpers import create_user, get_tokens
from motostore.models import Marca

class MarcaTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = create_user('admin_marca', is_staff=True)
        self.normal_user = create_user('user_marca')
        self.marca = Marca.objects.create(nombre='Honda', pais_origen='Japón')
        self.url = '/api/marcas/'

    def test_list_marcas_public(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)

    def test_create_marca_requires_admin(self):
        data = {'nombre': 'Yamaha'}
        resp = self.client.post(self.url, data)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        
        access, _ = get_tokens(self.normal_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        resp = self.client.post(self.url, data)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        
        access, _ = get_tokens(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        resp = self.client.post(self.url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
