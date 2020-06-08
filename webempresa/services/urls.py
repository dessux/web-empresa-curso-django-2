# Nuevo urls.py correspondiente a la app services
from django.urls import path
from . import views

urlpatterns = [
#    path('', views.services, name="services"),     # Se trasladó de urls.py en core
    path('', views.services, name="services"),      # Se trasladó de urls.py en core
]
