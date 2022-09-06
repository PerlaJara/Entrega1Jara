from django import forms
from app_blog.models import *

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    nombre_usuario = forms.CharField(max_length=100)
    correo = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput)


class PostFormulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    contenido = forms.CharField(widget=forms.Textarea)
    usuario_id = forms.ModelChoiceField(queryset=Usuario.objects.all())


class ComentarioFormulario(forms.Form):
    nombre_usuario = forms.CharField(max_length=100)
    comentario = forms.CharField(widget=forms.Textarea)
    id_usuario = forms.ModelChoiceField(queryset=Usuario.objects.all())
    post_id = forms.ModelChoiceField(queryset=Post.objects.all())    
