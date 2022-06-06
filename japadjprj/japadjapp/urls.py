from django.urls import path

from . import views;

urlpatterns = [
    path('/',views.index, name='index'),
    path('/inicio', views.login, name='login'),
    path('/validar', views.procesar, name='procesar'),
    path("/editar", views.editar_categoria, name="editar_cat"),
    path("/eliminar", views.eliminar_categoria, name="eliminar_cat")
]
