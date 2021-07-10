from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversor_num),
    path('binario', views.binario),
    path('hexadecimal', views.hexadecimal),
]