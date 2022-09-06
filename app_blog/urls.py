from django.urls import path

from app_blog import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('crear_usuario/', views.usuario_formulario, name="usuario_formulario"),
    path('crear_post/', views.post_formulario, name="post_formulario"),
    path('crear_comentario/', views.comentario_formulario, name="comentario_formulario"),
]    