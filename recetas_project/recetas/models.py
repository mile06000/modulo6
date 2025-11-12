from django.db import models

# Create your models here.
# recetas/models.py

from django.db import models
from django.urls import reverse

class Receta(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la receta")
    descripcion = models.TextField(max_length=300, verbose_name="Descripción breve")
    ingredientes = models.TextField(verbose_name="Ingredientes")
    instrucciones = models.TextField(verbose_name="Instrucciones de preparación")
    tiempo_preparacion = models.IntegerField(verbose_name="Tiempo de preparación (minutos)", default=30)
    porciones = models.IntegerField(verbose_name="Número de porciones", default=4)
    imagen = models.ImageField(upload_to='recetas/', verbose_name="Imagen de la receta", blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('receta_detalle', kwargs={'pk': self.pk})
