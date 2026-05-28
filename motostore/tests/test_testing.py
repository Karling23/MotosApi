from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from motostore.tests.helpers import create_user, get_tokens
from motostore.models import Marca, Categoria, Motocicleta, Testing

class TestingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = create_user('user1')
        marca = Marca.objects.create(nombre='Honda')
        cat = Categoria.objects.create(nombre='Sport')
        self.moto = Motocicleta.objects.create(
            marca=marca, categoria=cat, modelo='Moto', 
            anio=2023, cilindrada=600, color='Negro', precio=10000.00
        )

    def test_create_testing(self):
        access, _ = get_tokens(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        data = {
            'motocicleta': self.moto.id,
            'fecha_test': '2026-06-01T10:00:00Z',
        }
        resp = self.client.post('/api/testings/', data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
