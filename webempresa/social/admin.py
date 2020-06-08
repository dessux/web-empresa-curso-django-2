from django.contrib import admin

from .models import Link

# Register your models here.


# Métodos para modificar el modelo de Admin Django
#		https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-methods


# Crear un administrador de prueba
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # No permitir que se puedan modificar las claves de las redes sociales para prevenir que cualquier
    # usuario las modifique desde el panel del administrador Django
    
    # Extendemos la función para que los campos readonly_fields se puedan modif.
    def get_readonly_fields(self, request, obj=None):
        # Comprobar en tiempo de ejecución si hay un usuario identificado y si el usuario forma
        # parte del grupo personal
        if request.user.groups.filter(name="Personal").exists():
            # devolver el valor que tiene que sobreescribir a readonly_fields
            #return ('created', 'updated', 'key', 'name')
            return ('updated', 'key', 'name')
        else:   # Cualquier otro tipo de usuario
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)
