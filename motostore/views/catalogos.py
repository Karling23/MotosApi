from rest_framework import viewsets
from motostore.models import Marca, Categoria
from motostore.serializers import MarcaSerializer, CategoriaSerializer
from motostore.permissions import IsAdminOrReadOnly

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['nombre', 'descripcion', 'pais_origen']
    ordering_fields = ['nombre']

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['nombre']
