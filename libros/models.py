from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    editorial = models.CharField(max_length=150, blank=True, default="")
    anio = models.PositiveIntegerField()
    genero = models.CharField(max_length=100, blank=True, default="")
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ["-anio"]

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
