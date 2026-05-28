from rest_framework import viewsets
from motostore.models import Motocicleta, Casco, Accesorio
from motostore.serializers import MotocicletaSerializer, CascoSerializer, AccesorioSerializer
from motostore.permissions import IsAdminOrReadOnly
from motostore.filters import MotocicletaFilter, CascoFilter, AccesorioFilter

class MotocicletaViewSet(viewsets.ModelViewSet):
    queryset = Motocicleta.objects.all()
    serializer_class = MotocicletaSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = MotocicletaFilter
    search_fields = ['modelo', 'descripcion']
    ordering_fields = ['precio', 'anio', 'cilindrada']

class CascoViewSet(viewsets.ModelViewSet):
    queryset = Casco.objects.all()
    serializer_class = CascoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = CascoFilter
    search_fields = ['modelo', 'descripcion', 'certificacion']
    ordering_fields = ['precio']

class AccesorioViewSet(viewsets.ModelViewSet):
    queryset = Accesorio.objects.all()
    serializer_class = AccesorioSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = AccesorioFilter
    search_fields = ['nombre', 'descripcion', 'categoria_accesorio']
    ordering_fields = ['precio']
