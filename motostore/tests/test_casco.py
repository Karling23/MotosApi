from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from motostore.models import Marca, Casco

class CascoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.marca = Marca.objects.create(nombre='AGV')
        self.casco = Casco.objects.create(
            marca=self.marca, modelo='K3', talla='M',
            color='Negro', precio=200.00
        )

    def test_list_cascos(self):
        resp = self.client.get('/api/cascos/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)
