from django.db import models

#from django.utils.timezone import now               # Permitir maneno de la zona horaria actual para las fechas
from django.utils import timezone      # Permitir maneno de la zona horaria actual para las fechas

from django.contrib.auth.models import User         # User contiene todos lo usuario regristrados en el panel de Administrador

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']             # Prefijo "-" para ordenar a la inversa

    # Devolver el nombre de la categoría
    def __str__(self):
        return self.name

# Modelo para la entrada
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    #published = models.DateTimeField(verbose_name="Fecha de publicación",default=now)
    published = models.DateTimeField(verbose_name="Fecha de publicación",default=timezone.now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    # Impotar author del modelo user
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)    # Borrar en cascada todas las entradas que tenía este autor
    # author = models.ForeignKey(User,verbose_name="Autor",on_delete=models.PROTECT)    # Protege a este campo de ser borrado pero se debe tener el campo como  null=True, blank=True para que se quede en blanco
    # Permitir escoger varias categorías para una entrada
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts") # related_name es el nombre para consulta inversa en la relación ManyToMany
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")  

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']             # Prefijo "-" para ordenar a la inversa

    # Devolver el título de la categoría
    def __str__(self):
        return self.title
