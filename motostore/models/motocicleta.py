from django.db import models
from .marca import Marca
from .categoria import Categoria

class Motocicleta(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='motocicletas')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='motocicletas')
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    cilindrada = models.IntegerField(help_text="Cilindrada en cc")
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.marca.nombre} {self.modelo} ({self.anio})"
