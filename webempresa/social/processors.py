# Procesadores de contexto

from .models import Link

# Procesador de contexto para extender el diccionario
def ctx_dict(request):
    '''
    # Declaramos un diccionario de prueba (es un ejemplo de la iyección del diccionario y que se defini común a todas las páginas)
    #ctx = {'test': 'hola'}
    return ctx
    '''

    ctx = {}
    links = Link.objects.all()               # Buscar los links y recorrer cada enlace
    
    # Generar un diccionario con las redes sociales y su clave (ctx[link.key]) y sus valores (links.url)
    for link in links:
        ctx[link.key] = link.url

    return ctx

# Agregar en TEMPLATES de settings.py y en 'context_processors' -> 'social.processors.ctx_dict'