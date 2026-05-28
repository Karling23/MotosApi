from django.db import models
from .marca import Marca

class Casco(models.Model):
    TALLAS_CHOICES = [
        ('XS', 'XS'), ('S', 'S'), ('M', 'M'), 
        ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')
    ]
    
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='cascos')
    modelo = models.CharField(max_length=100)
    talla = models.CharField(max_length=10, choices=TALLAS_CHOICES)
    color = models.CharField(max_length=50)
    certificacion = models.CharField(max_length=100, blank=True, null=True, help_text="Ej: DOT, ECE 22.05")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Casco {self.marca.nombre} {self.modelo} - Talla {self.talla}"
