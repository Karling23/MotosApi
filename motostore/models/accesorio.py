from django.db import models
from .marca import Marca

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True, related_name='accesorios')
    categoria_accesorio = models.CharField(max_length=100, help_text="Ej: Guantes, Chaqueta, Candados")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
