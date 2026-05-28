from rest_framework import serializers
from motostore.models import Motocicleta
from .marca import MarcaSerializer
from .categoria import CategoriaSerializer

class MotocicletaSerializer(serializers.ModelSerializer):
    # Optional: If you want nested representations on GET, but allow ID on POST
    marca_detalle = MarcaSerializer(source='marca', read_only=True)
    categoria_detalle = CategoriaSerializer(source='categoria', read_only=True)

    class Meta:
        model = Motocicleta
        fields = '__all__'
