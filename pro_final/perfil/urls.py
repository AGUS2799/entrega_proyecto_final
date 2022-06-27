from django.urls import path

from perfil import views


app_name='perfil'
urlpatterns = [
    path('<int:id>', views.datos_del_perfil, name='perfil'),
    
]