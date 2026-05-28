from django.db import models
from .usuario import Usuario
from .motocicleta import Motocicleta
from .casco import Casco
from .accesorio import Accesorio

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    direccion_envio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username} - {self.estado}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    motocicleta = models.ForeignKey(Motocicleta, on_delete=models.SET_NULL, null=True, blank=True)
    casco = models.ForeignKey(Casco, on_delete=models.SET_NULL, null=True, blank=True)
    accesorio = models.ForeignKey(Accesorio, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de Pedido #{self.pedido.id}"
