from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from motostore.models import Accesorio

class AccesorioTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.accesorio = Accesorio.objects.create(
            nombre='Guantes', categoria_accesorio='Ropa', precio=50.00
        )

    def test_list_accesorios(self):
        resp = self.client.get('/api/accesorios/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)
