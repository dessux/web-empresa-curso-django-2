from django.contrib import admin

from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    # Crear campos de solo lectura para created y updated
    readonly_fields = ('created', 'updated')

# Registrar el servicio y su configuración
admin.site.register(Service, ServiceAdmin)