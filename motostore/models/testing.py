from django.db import models
from .usuario import Usuario
from .motocicleta import Motocicleta

class Testing(models.Model):
    ESTADO_CHOICES = [
        ('programado', 'Programado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='testings')
    motocicleta = models.ForeignKey(Motocicleta, on_delete=models.CASCADE, related_name='testings')
    fecha_test = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='programado')
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Test {self.id} - {self.usuario.username} - {self.motocicleta.modelo}"
