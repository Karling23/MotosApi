from django_filters import rest_framework as filters
from motostore.models import Motocicleta, Casco, Accesorio, Pedido, Testing

class MotocicletaFilter(filters.FilterSet):
    precio_min = filters.NumberFilter(field_name="precio", lookup_expr='gte')
    precio_max = filters.NumberFilter(field_name="precio", lookup_expr='lte')
    
    class Meta:
        model = Motocicleta
        fields = ['marca', 'categoria', 'anio', 'cilindrada']

class CascoFilter(filters.FilterSet):
    precio_min = filters.NumberFilter(field_name="precio", lookup_expr='gte')
    precio_max = filters.NumberFilter(field_name="precio", lookup_expr='lte')

    class Meta:
        model = Casco
        fields = ['marca', 'talla', 'color']

class AccesorioFilter(filters.FilterSet):
    precio_min = filters.NumberFilter(field_name="precio", lookup_expr='gte')
    precio_max = filters.NumberFilter(field_name="precio", lookup_expr='lte')

    class Meta:
        model = Accesorio
        fields = ['marca', 'categoria_accesorio']

class PedidoFilter(filters.FilterSet):
    fecha_desde = filters.DateFilter(field_name="fecha_pedido", lookup_expr='gte')
    fecha_hasta = filters.DateFilter(field_name="fecha_pedido", lookup_expr='lte')

    class Meta:
        model = Pedido
        fields = ['estado', 'usuario']

class TestingFilter(filters.FilterSet):
    fecha_desde = filters.DateFilter(field_name="fecha_test", lookup_expr='gte')
    fecha_hasta = filters.DateFilter(field_name="fecha_test", lookup_expr='lte')

    class Meta:
        model = Testing
        fields = ['estado', 'usuario', 'motocicleta']
