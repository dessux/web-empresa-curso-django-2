from django.contrib import admin

# Crear un administrador para nuestro blog
from .models import Category, Post

# Register your models here.
# Categorías
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
#    readonly_fields : ['created', 'updated']

# Entradas
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Personalizando el administrador:
    list_display = ('title', 'author', 'published', 'post_categories') # Mostrar columnas en el Admin
    ordering = ('author', 'published')                  # (Tuplas) Ordena por las cols. author (1) y published (2). Si es un solo campo por el que se ordena se debe poner al final la ","
    search_fields = ('title','content','author__username', 'categories__name') # Mostrar formulario de búsqueda a partir de unos campos. Como author es un campo relacionado se debe indicar buscar username de author (author__username)
    date_hierarchy = 'published'                        # Jerarquizar por fechas
    list_filter = ('author__username','categories__name') # El filtrado tiene mas sentido usarlo en relaciones ya que es donde se pueden repetir ocurrencias o registros

    # Para campos que son manytomany podemos crear nuestros campos:
    def post_categories(self, obj):                     # obj es el registro o fila
        #return 'ALGO'                                   # ALGO es mostrado en la columna post_categories

        print ("obj: ", obj)
        print ("obj.categories: ", obj.categories)
        for cat in obj.categories.all():
            print("cat: ",cat)
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])   # Sacar el nombre (c.name) para cada categoria (c) en todas las categorías (obj.categories.all())

    # Documentación para inyectar html en el contenido https://stackoverflow.com/questions/47953705/how-do-i-use-allow-tags-in-django-2-0-admin

    # Para colocar un nombre propio a columna post_categories sobreescribimos un atributo
    post_categories.short_description = "Categorías"

# Registrar los cambios en el administrador para Category
admin.site.register(Category, CategoryAdmin)
# Registrar los cambios en el administrador para la entrada Post
admin.site.register(Post, PostAdmin)
