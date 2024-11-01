from django.db import models
from decimal import Decimal

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    descripcion_corta = models.TextField( null=True, blank=True)
    img = models.ImageField(upload_to='proyectos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='vehiculos')
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='vehiculos/')
    km_por_galon = models.DecimalField(max_digits=5, decimal_places=2)
    kilometros_usados = models.PositiveIntegerField(default=0)
    precio_combustible = models.DecimalField(max_digits=5, decimal_places=2)

    def gasto_total(self):
        if self.km_por_galon > 0:
            # Convertir a Decimal el precio del combustible y los kilómetros usados
            galones_usados = Decimal(self.kilometros_usados) / Decimal(self.km_por_galon)
            total_gasto = galones_usados * Decimal(self.precio_combustible)
            return round(total_gasto, 2)
        return Decimal(0)  # Asegurarse de que el retorno sea Decimal

    def __str__(self):
        return self.nombre