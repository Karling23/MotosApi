from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from motostore.tests.helpers import create_user, get_tokens
from motostore.models import Categoria

class CategoriaTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = create_user('admin_cat', is_staff=True)
        Categoria.objects.create(nombre='Deportivas')
        self.url = '/api/categorias/'

    def test_list_categorias(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)

    def test_create_categoria_admin(self):
        access, _ = get_tokens(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        resp = self.client.post(self.url, {'nombre': 'Cruiser'})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
