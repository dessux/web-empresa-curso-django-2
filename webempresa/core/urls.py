# Organizando mejor las url's del proyecto

from django.urls import path
from . import views

urlpatterns = [
    # Paths del core
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
#    path('services/', views.services, name="services"),    Se traslada al nuevo urls.py de su app (services)
    path('store/', views.store, name="store"),
#    path('contact/', views.contact, name="contact"),       Se traslada al nuevo urls.py de su app (contact)
#    path('blog/', views.blog, name="blog"),                Se traslada al nuevo urls.py de su app (blog)
#    path('sample/', views.sample, name="sample"),          Se traslada al nuevo urls.py de su app (pages)
]
