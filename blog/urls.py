from django.urls import path
from . import views

urlpatterns = [
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_post/', views.agregar_post, name='agregar_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
