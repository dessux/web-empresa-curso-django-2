from django.shortcuts import render

# Para acceder al modelo
from .models import Service

# Create your views here.
def services(request):

    # Crear la lista de servicios para poder fusionarla con los datos de la BD
    services = Service.objects.all()

    #return HttpResponse("Servicios")
    return render(request, "services/services.html", {'services':services})
