from rest_framework import serializers
from motostore.models import Motocicleta
from .marca import MarcaSerializer
from .categoria import CategoriaSerializer

class MotocicletaSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Motocicleta
        fields = ['id', 'modelo', 'precio', 'stock', 'is_active']

class MotocicletaSerializer(serializers.ModelSerializer):
    marca_detalle = MarcaSerializer(source='marca', read_only=True)
    categoria_detalle = CategoriaSerializer(source='categoria', read_only=True)
    precio_con_iva = serializers.SerializerMethodField()
    in_stock = serializers.SerializerMethodField()

    class Meta:
        model = Motocicleta
        fields = [
            'id', 'marca', 'categoria', 'modelo', 'anio', 'cilindrada', 
            'color', 'precio', 'precio_con_iva', 'stock', 'in_stock', 
            'is_active', 'descripcion', 'marca_detalle', 'categoria_detalle'
        ]
        read_only_fields = ['id']

    def get_precio_con_iva(self, obj):
        return round(float(obj.precio) * 1.15, 2) if obj.precio else 0

    def get_in_stock(self, obj):
        return obj.stock > 0

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError('El precio debe ser mayor a 0.')
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('El stock no puede ser negativo.')
        return value
