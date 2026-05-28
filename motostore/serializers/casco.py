from rest_framework import serializers
from motostore.models import Casco
from .marca import MarcaSerializer

class CascoSerializer(serializers.ModelSerializer):
    marca_detalle = MarcaSerializer(source='marca', read_only=True)

    class Meta:
        model = Casco
        fields = '__all__'
