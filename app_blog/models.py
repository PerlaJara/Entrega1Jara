from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}, {self.nombre_usuario}'


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = RichTextField(blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario_id = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.titulo}'


class Comentario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
