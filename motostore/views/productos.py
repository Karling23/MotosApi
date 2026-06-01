from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from django.db.models import Avg, Max, Min, Sum, Count

from motostore.models import Motocicleta, Casco, Accesorio
from motostore.serializers import (
    MotocicletaSerializer, MotocicletaSummarySerializer,
    CascoSerializer, CascoSummarySerializer,
    AccesorioSerializer, AccesorioSummarySerializer
)
from motostore.permissions import IsAdminOrReadOnly
from motostore.filters import MotocicletaFilter, CascoFilter, AccesorioFilter

class BaseProductViewSet(viewsets.ModelViewSet):
    """
    Base viewset for products to share common custom actions.
    """
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser], url_path='restock')
    def restock(self, request, pk=None):
        product = self.get_object()
        try:
            quantity = int(request.data.get('quantity', 0))
            if quantity <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return Response(
                {'error': 'La cantidad debe ser un entero positivo.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        product.stock += quantity
        product.save(update_fields=['stock'])
        return Response({
            'id': product.id,
            'nuevo_stock': product.stock,
        })

    @action(detail=False, methods=['get'], permission_classes=[AllowAny], url_path='available')
    def available(self, request):
        qs = self.filter_queryset(
            self.get_queryset().filter(stock__gt=0, is_active=True)
        )
        page = self.paginate_queryset(qs)
        if page is not None:
            return self.get_paginated_response(
                self.summary_serializer_class(page, many=True).data
            )
        return Response(self.summary_serializer_class(qs, many=True).data)

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        qs = self.get_queryset()
        active = qs.filter(is_active=True)
        data = active.aggregate(
            total_active = Count('id'),
            avg_precio = Avg('precio'),
            max_precio = Max('precio'),
            min_precio = Min('precio'),
            total_stock = Sum('stock'),
        )
        data['total_inactive'] = qs.filter(is_active=False).count()
        data['out_of_stock'] = active.filter(stock=0).count()
        if data['avg_precio']:
            data['avg_precio'] = round(float(data['avg_precio']), 2)
        return Response(data)

class MotocicletaViewSet(BaseProductViewSet):
    queryset = Motocicleta.objects.all()
    serializer_class = MotocicletaSerializer
    summary_serializer_class = MotocicletaSummarySerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = MotocicletaFilter
    search_fields = ['modelo', 'descripcion']
    ordering_fields = ['precio', 'anio', 'cilindrada']

class CascoViewSet(BaseProductViewSet):
    queryset = Casco.objects.all()
    serializer_class = CascoSerializer
    summary_serializer_class = CascoSummarySerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = CascoFilter
    search_fields = ['modelo', 'descripcion', 'certificacion']
    ordering_fields = ['precio']

class AccesorioViewSet(BaseProductViewSet):
    queryset = Accesorio.objects.all()
    serializer_class = AccesorioSerializer
    summary_serializer_class = AccesorioSummarySerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = AccesorioFilter
    search_fields = ['nombre', 'descripcion', 'categoria_accesorio']
    ordering_fields = ['precio']
