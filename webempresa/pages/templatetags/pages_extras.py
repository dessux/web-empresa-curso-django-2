# Documentación de template tags personalizados:
# https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/

# Regitrar pages_extras.py dentro de la librería de templates
from django import template
from pages.models import Page

# Registrar el template tag (de get_page_list()) en la librería de templates
register = template.Library()

# Crear un nuevo template donde hacer uso de esta página
@register.simple_tag            # Decorador para implementar una nueva funcionalidad transformado a simple_tag y se registra en la librería de templates
def get_page_list():
    pages = Page.objects.all()

    return pages        # Se devuelve al template en forma de template tag

# Es necesario detener y reiniciar el servidor para que tome estos cambios y los mantenga en memoria
