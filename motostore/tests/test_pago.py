from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from motostore.tests.helpers import create_user, get_tokens
from motostore.models import Pedido, Pago

class PagoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = create_user('user1')
        self.pedido = Pedido.objects.create(usuario=self.user1, total=10000.00)

    def test_create_pago(self):
        access, _ = get_tokens(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        data = {
            'pedido': self.pedido.id,
            'metodo_pago': 'tarjeta',
            'monto': '10000.00'
        }
        resp = self.client.post('/api/pagos/', data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
