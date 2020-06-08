from django.urls import path
from . import views
 
# /<slug:page_slug> de page.title|slugify en la vista se agrega como adorno para poner en la url 
# el título de la página separado por guiones (modo slug)
urlpatterns = [
    path('<int:page_id>/<slug:page_slug>', views.page, name="page"),
]
