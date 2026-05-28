from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from motostore.tests.helpers import create_user, get_tokens
from motostore.models import Pedido, Motocicleta, Marca, Categoria

class PedidoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = create_user('user1')
        self.user2 = create_user('user2')
        marca = Marca.objects.create(nombre='Honda')
        cat = Categoria.objects.create(nombre='Sport')
        self.moto = Motocicleta.objects.create(
            marca=marca, categoria=cat, modelo='Moto', 
            anio=2023, cilindrada=600, color='Negro', precio=10000.00
        )
        self.pedido = Pedido.objects.create(usuario=self.user1, total=10000.00)

    def test_list_pedidos_owner_only(self):
        access, _ = get_tokens(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        resp = self.client.get('/api/pedidos/')
        self.assertEqual(len(resp.data['results']), 1)
        
        access, _ = get_tokens(self.user2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        resp = self.client.get('/api/pedidos/')
        self.assertEqual(len(resp.data['results']), 0)

    def test_create_pedido(self):
        access, _ = get_tokens(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        data = {
            'direccion_envio': 'Test Address',
            'detalles_data': [
                {'motocicleta': self.moto.id, 'cantidad': 1, 'precio_unitario': '10000.00'}
            ]
        }
        resp = self.client.post('/api/pedidos/', data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(float(resp.data['total']), 10000.00)
