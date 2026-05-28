from rest_framework import serializers
from motostore.models import Accesorio
from .marca import MarcaSerializer

class AccesorioSerializer(serializers.ModelSerializer):
    marca_detalle = MarcaSerializer(source='marca', read_only=True)

    class Meta:
        model = Accesorio
        fields = '__all__'
