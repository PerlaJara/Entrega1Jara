from django import forms
from app_blog.models import *

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    nombre_usuario = forms.CharField(max_length=100)
    correo = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput)
    fecha_creacion = forms.DateField()


class PostFormulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    contenido = forms.CharField(widget=forms.Textarea)
    #fecha_creacion = forms.DateField()
    usuario_id = forms.ModelChoiceField(queryset=Usuario.objects.all())
