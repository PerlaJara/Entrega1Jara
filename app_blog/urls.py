from django.urls import path

from app_blog import views

urlpatterns = [
    #Main URL
    path('', views.inicio, name="inicio"),

    #URL's user
    path('usuario/', views.usuario, name="usuario"),
    path('crear_usuario/', views.usuario_formulario, name="crear_usuario"),
    path('buscar_usuario_form/', views.buscar_usuario_form, name="buscar_usuario_form"),
    path('buscar_usuario/', views.buscar_usuario, name="buscar_usuario"),

    #URL's post
    path('crear_post/', views.post_formulario, name="crear_post"),

    #URL's comentario
    path('crear_comentario/', views.comentario_formulario, name="crear_comentario"),
]