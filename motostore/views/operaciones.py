from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from motostore.models import Pedido, Pago, Testing
from motostore.serializers import PedidoSerializer, PagoSerializer, TestingSerializer
from motostore.permissions import IsOwnerOrAdmin
from motostore.filters import PedidoFilter, TestingFilter

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    filterset_class = PedidoFilter
    ordering_fields = ['fecha_pedido', 'total']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Pedido.objects.all()
        return Pedido.objects.filter(usuario=user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class PagoViewSet(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    ordering_fields = ['fecha_pago', 'monto']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Pago.objects.all()
        return Pago.objects.filter(pedido__usuario=user)

class TestingViewSet(viewsets.ModelViewSet):
    serializer_class = TestingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    filterset_class = TestingFilter
    ordering_fields = ['fecha_test']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Testing.objects.all()
        return Testing.objects.filter(usuario=user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
