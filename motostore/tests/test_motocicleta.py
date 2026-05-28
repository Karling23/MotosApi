from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from motostore.tests.helpers import create_user, get_tokens
from motostore.models import Marca, Categoria, Motocicleta

class MotocicletaTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = create_user('admin_moto', is_staff=True)
        self.marca = Marca.objects.create(nombre='Honda')
        self.categoria = Categoria.objects.create(nombre='Sport')
        self.moto = Motocicleta.objects.create(
            marca=self.marca, categoria=self.categoria,
            modelo='CBR600RR', anio=2023, cilindrada=600,
            color='Rojo', precio=12000.00
        )

    def test_list_motocicletas(self):
        resp = self.client.get('/api/motocicletas/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)

    def test_create_motocicleta_admin(self):
        access, _ = get_tokens(self.admin)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        data = {
            'marca': self.marca.id,
            'categoria': self.categoria.id,
            'modelo': 'CBR1000RR',
            'anio': 2024,
            'cilindrada': 1000,
            'color': 'Azul',
            'precio': '15000.00'
        }
        resp = self.client.post('/api/motocicletas/', data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
