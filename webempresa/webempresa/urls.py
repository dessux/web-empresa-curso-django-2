"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core import views

from django.conf import settings

''' Vistas / URLS a crear:
Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/ (esta es para páginas de prueba)
'''

urlpatterns = [
# Trasladamos los paths del core al nuevo archivo core/urls.py

#    # Paths del core
#    path('', views.home, name="home"),
#    path('about/', views.about, name="about"),
#    path('services/', views.services, name="services"),
#    path('store/', views.store, name="store"),
#    path('contact/', views.contact, name="contact"),
#    path('blog/', views.blog, name="blog"),
#    path('sample/', views.sample, name="sample"),

    # Paths del core (Forma usada para organizar mejor las urls) - como indica en Including another URLconf -
    # path('core/', include('core.urls')), 
     path('', include('core.urls')),  # Quitando 'core/' del 1er. param. evitamos usar core/ en el path de la url

    # Paths de services
    path('services/', include('services.urls')),

    # Paths de blog
    path('blog/', include('blog.urls')),

    # Paths de pages
    path('page/', include('pages.urls')),

    # Paths de contact
    path('contact/', include('contact.urls')),

    # Paths del admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static  # Cargar el módulo que servirá archivos estàticos
    # Servir archivos media de MEDIA_URL que serán busacdos en el dir. MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
