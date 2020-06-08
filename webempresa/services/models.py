from django.db import models

# Create your models here.

# Agregar el modelo de servicio y agregar los campos
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Subtitulo", upload_to="services")   # Cargar las imagenes al directorio services dentro de media
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']             # Prefijo "-" para ordenar a la inversa

    # Devolver el título del servicio
    def __str__(self):
        return self.title
