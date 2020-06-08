from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)    # Campo sulgField obliga a utilizar caracteres alfanuméricos, guiones o barras
    name = models.CharField(verbose_name="Red social", max_length=200)                  # Nombre de la Red Social
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")  

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']             # Ordenar por nombre

    # Devolver el título del Link
    def __str__(self):
        return self.name
