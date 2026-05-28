from rest_framework import serializers
from motostore.models import Pedido, DetallePedido
from .motocicleta import MotocicletaSerializer
from .casco import CascoSerializer
from .accesorio import AccesorioSerializer

class DetallePedidoSerializer(serializers.ModelSerializer):
    motocicleta_detalle = MotocicletaSerializer(source='motocicleta', read_only=True)
    casco_detalle = CascoSerializer(source='casco', read_only=True)
    accesorio_detalle = AccesorioSerializer(source='accesorio', read_only=True)

    class Meta:
        model = DetallePedido
        fields = '__all__'
        read_only_fields = ['pedido']

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)
    
    detalles_data = serializers.ListField(
        child=serializers.DictField(), write_only=True, required=False
    )

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'fecha_pedido', 'estado', 'total', 'direccion_envio', 'detalles', 'detalles_data']
        read_only_fields = ['id', 'usuario', 'fecha_pedido']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles_data', [])
        pedido = Pedido.objects.create(**validated_data)
        
        total_calculado = 0
        for detalle in detalles_data:
            precio_unitario = detalle.get('precio_unitario', 0)
            cantidad = detalle.get('cantidad', 1)
            
            fk_fields = ['motocicleta', 'casco', 'accesorio']
            create_kwargs = {'pedido': pedido, 'cantidad': cantidad, 'precio_unitario': precio_unitario}
            for field in fk_fields:
                if field in detalle:
                    create_kwargs[f"{field}_id"] = detalle[field]
            
            DetallePedido.objects.create(**create_kwargs)
            total_calculado += float(precio_unitario) * cantidad
            
        if total_calculado > 0:
            pedido.total = total_calculado
            pedido.save()
            
        return pedido
