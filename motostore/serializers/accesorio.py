from rest_framework import serializers
from motostore.models import Accesorio
from .marca import MarcaSerializer

class AccesorioSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesorio
        fields = ['id', 'nombre', 'precio', 'stock', 'is_active']

class AccesorioSerializer(serializers.ModelSerializer):
    marca_detalle = MarcaSerializer(source='marca', read_only=True)
    precio_con_iva = serializers.SerializerMethodField()
    in_stock = serializers.SerializerMethodField()

    class Meta:
        model = Accesorio
        fields = [
            'id', 'nombre', 'marca', 'categoria_accesorio',
            'precio', 'precio_con_iva', 'stock', 'in_stock',
            'is_active', 'descripcion', 'marca_detalle'
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
