from django.db import models
from ckeditor.fields import RichTextField       # Funcionalidad para editor CKEditor

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)                  # Título de la página
    
    #content = models.TextField(verbose_name="Contenido")
    # El contenido es el que queremos sustituir por el editor Wiziwig (CKEditor)
    content = RichTextField(verbose_name="Contenido")

    # Método para ordenar las páginas desde el Administrador, agregando un campo nuevo (order) al modelo
    order = models.SmallIntegerField(verbose_name="Orden", default=0)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")  

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']             # Ordenar por página(irder) y por título (title)

    # Devolver el título de la página
    def __str__(self):
        return self.title
