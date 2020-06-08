from django.shortcuts import render, redirect       # redirect se utiliza para redireccionar páginas

from django.urls import reverse                     # reverse es equivalente al template tag url

from django.core.mail import EmailMessage           # Crear la estructura de un mensaje e incluye un método para enviarlo

from .forms import ContactForm

# Desde su vista lo pasamos al template

# Create your views here.
def contact(request):
    # Verificar el tipo de petición enviado desde el html (POST o GET)
    #print ("Tipo de petición: {}".format(request.method)) 

    contact_form = ContactForm()                        # Instanciamos el formulario (Crea la plantilla vacía)

    # Procesar el formular únicamente cuando se realice por una petición tipo POST
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)   # Generamos un formulario ContactForm pasásandole un campo tipo data con el diccionario que hay en request.POST (los datos capturados en el formulario). Formulario con los datos rellenados
        # Comprobar que todos los campos llenados son correctos
        if contact_form.is_valid():
            # Si los campos son correctos los recuperamos:
            name = request.POST.get('name', '')         # Si no hay name devuelve una cadena vacía
            email = request.POST.get('email', '')       # Si no hay email devuelve una cadena vacía
            content = request.POST.get('content', '')   # Si no hay content devuelve una cadena vacía

            # Enviar el email

            '''
            # Por ahora suponemos que todo ha ido bien, hacemos un redireccionamiento
            #return redirect('/contact/?ok')             # Redirecciona a la página contact con una variable de tipo GET con un ok, que detectaremos en el template para mostrar un mensaje que diga que ha enviado correctamente
            return redirect(reverse('contact')+'?ok')   # Es equivalente al template tag url
            '''

            # Enviamos el correo y direccionamos
            # Clase para enviar el correo
            '''
            email = EmailMessage(
                asunto,                 # Mensaje de contacto
                cuerpo,                 # Estructura con datos de correo de la persona que nos quiere contactar (De: A: Contenido)
                email_origen,           # Correo de la empresa que concuerde con el que se tiene configurado
                email_destino,          # Agregar lista con todas las cuentas de correo que se requiera enviar el mensaje
                reply_to=[email]
            )
            '''

            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["sftwdev@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+'?ok')       # Es equivalente al template tag url, en el template evaluamos ok
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+'?fail')     # Es equivalente al template tag url, en el template evaluamos fail


    #return HttpResponse("Contacto")
    return render(request, "contact/contact.html", {'form': contact_form})  # Con el param. {'form': contact_form} enviamos el formulario al template para enviar un mensaje donde se notifique que algo a fallado con el envío del correo

