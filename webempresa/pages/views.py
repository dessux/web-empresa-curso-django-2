from django.shortcuts import render, get_object_or_404

from .models import Page

# Create your views here.

# Parmámetro page_slug de page.title|slugify en la vista se agrega como adorno para poner en la 
# url el título de la página separado por guiones (modo slug)
def page(request, page_id, page_slug):
    #return HttpResponse("Sample")
    page = get_object_or_404(Page, id=page_id)

    return render(request, 'pages/sample.html', {'page': page})