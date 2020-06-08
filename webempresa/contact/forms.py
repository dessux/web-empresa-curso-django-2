from django import forms

# 		- Documentación oficial sobre forms Django:
#			https://docs.djangoproject.com/en/2.0/topics/forms/

# 		- Documentación oficial sobre dibujar campos del formulario  Django:
#			https://docs.djangoproject.com/en/2.0/topics/forms/#rendering-fields-manually


# Es parecido a crear un modelo
class ContactForm(forms.Form):
    # Crear los campos del formulario
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}), min_length=3, max_length=100)   # Con widget agregamos una clase extendida
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Escribe tu email'}), min_length=3, max_length=100)   # Con forms.EmailInput conservar la prevalidación de forms.EmailField
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu mensaje'}), min_length=10, max_length=1000) # A diferencia de los models para textos cortos o largos se usa CharField(). Máximo 3 renglones en el TextArea de Content

