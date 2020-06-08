
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    # Se añade path para agregar el id de categoria (category_id)
    path('category/<int:category_id>/', views.category, name="category"),   # Con <category_id> (se forza a un entero con int) se toma el campo como dinámico y se lo pasa a la vista def category(request, category_id)
]

# Documentación para conversiones disponibles en Django
# https://docs.djangoproject.com/en/2.0/topics/http/urls/#path-converters