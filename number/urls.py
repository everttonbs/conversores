from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversor_num),
    
]