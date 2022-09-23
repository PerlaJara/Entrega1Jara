from django.contrib import admin

# Register your models here.
from app_blog.models import Usuario, Post, Comentario

admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Comentario)