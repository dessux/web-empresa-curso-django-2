from django.contrib import admin

from .models import Page

# Register your models here.

# Crear un administrador de prueba
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')           # Nos permitirá modificar el orden de las páginas secundarias

admin.site.register(Page, PageAdmin)
