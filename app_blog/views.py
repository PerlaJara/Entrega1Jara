from typing import Dict

from django.shortcuts import render
from django.http import HttpResponse

from app_blog.models import *
from app_blog.forms import *

# Create your views here.
def inicio(request):
    return render(request, "app_blog/inicio.html")


def usuario_formulario(request):
    if request.method == 'POST':
        formulario= UsuarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = Usuario(nombre=data['nombre'], apellido=data['apellido'], nombre_usuario=data['nombre_usuario'], correo=data['correo'], contrasena=data['contrasena'])
            usuario.save()
            return render(request, "app_blog/inicio.html", {"exitoso": True})
    else: 
        formulario= UsuarioFormulario()
    return render(request, "app_blog/crear_usuario.html", {"formulario": formulario})


def post_formulario(request):
    if request.method == 'POST':
        formulario= PostFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            post = Post(titulo=data['titulo'], contenido=data['contenido'], usuario_id=data['usuario_id'])
            post.save()
            return render(request, "app_blog/inicio.html", {"exitoso": True})
    else:
        formulario= PostFormulario()
    return render(request, "app_blog/crear_post.html", {"formulario": formulario})


def comentario_formulario(request):
    if request.method == 'POST':
        formulario= ComentarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            comentario = Comentario(nombre_usuario=data['nombre_usuario'], comentario=data['comentario'],id_usuario=data['id_usuario'], post_id=data['post_id'])
            comentario.save()
            return render(request, "app_blog/inicio.html", {"exitoso": True})
    else:
        formulario= ComentarioFormulario()
    return render(request, "app_blog/crear_comentario.html", {"formulario": formulario})    