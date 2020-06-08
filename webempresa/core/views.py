#from django.shortcuts import render, HttpResponse
from django.shortcuts import render

# Create your views here.

''' Vistas a crear:
Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/ (esta es para páginas de prueba)
'''

# Las definiciones son termporales y al hacer las apps de cada una, las func. se moverán 
# a sus correspondientes views y solo quedarán las páginas estáticas (que no varían,
# que son Portada, Historia, Visitanos y Contacto)

def home(request):
    #return HttpResponse("Inicio")
    return render(request, "core/home.html")

def about(request):
    #return HttpResponse("Historia")
    return render(request, "core/about.html")

# Se traslada services a la vista de su app services
#def services(request):
#    #return HttpResponse("Servicios")
#    return render(request, "core/services.html")

def store(request):
    #return HttpResponse("Visítanos")
    return render(request, "core/store.html")

# Se traslada contact a la vista de su app contact
#def contact(request):
#    #return HttpResponse("Contacto")
#    return render(request, "core/contact.html")

# Se traslada blog a la vista de su app blog
#def blog(request):
#    #return HttpResponse("Blog")
#    return render(request, "core/blog.html")

# Se traslada sample a la vista de su app pages
#def sample(request):
#    #return HttpResponse("Sample")
#    return render(request, "core/sample.html")
