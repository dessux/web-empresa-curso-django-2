
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.contact, name="contact"),       # Se trasladó desde urls.py core
]
