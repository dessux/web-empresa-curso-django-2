from django.shortcuts import render, get_object_or_404  # get_object_or_404 se usa para controlar excepciones de mensajes de error cuando no existe la página (404).

# Para acceder al modelo
from .models import Post, Category

# Create your views here.

def blog(request):

    # Importar las entradas para mostrarlas en el blog del html
    posts = Post.objects.all()

    #return HttpResponse("Blog")
    return render(request, "blog/blog.html", {'posts':posts})    # {'posts':post} Pasa el resultado del query a la página blog.html
    
# Vista category
def category(request, category_id):

    #category = Category.objects.get(id=category_id)             # Recuperar el category_id
    # Transformanndo Category.objects.get para capturar errores 404 (Forma rudimentaria)
    category = get_object_or_404(Category, id=category_id)       # Recuperar el category_id

    '''
    # Buscar las entradas para pasarlas al template (Con Consulta para recuperarlas, filtrando por categoría)
    posts = Post.objects.filter(categories=category)

    return render(request, "blog/category.html", {'category':category, 'posts':posts})
    '''

    # Django ofrece una manera mas sencilla de realizar la consulta, 
    # gracias a las relaciones que tiene la capacidad de hacer consultas inversas
    return render(request, "blog/category.html", {'category':category})
