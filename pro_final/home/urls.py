from django.contrib import admin
from django.urls import path
from home import views


app_name='home'
urlpatterns = [
    path('',views.home, name='Home'),
    path('about/',views.about, name='about'),
]
