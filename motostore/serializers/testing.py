from rest_framework import serializers
from motostore.models import Testing
from .motocicleta import MotocicletaSerializer

class TestingSerializer(serializers.ModelSerializer):
    motocicleta_detalle = MotocicletaSerializer(source='motocicleta', read_only=True)

    class Meta:
        model = Testing
        fields = '__all__'
        read_only_fields = ['id', 'usuario']
