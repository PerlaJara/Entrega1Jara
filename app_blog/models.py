from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=50)
    fecha_creacion = models.DateField()


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_creacion = models.DateField()
    usuario_id = models.ForeignKey('Usuario', on_delete=models.CASCADE)


class Comentario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
