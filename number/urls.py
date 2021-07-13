from django.urls import path
from .views import views

urlpatterns = [
    path('', views.index),
    path('número', views.convert_num),
    path('comprimento', views.unit_lenght)
    
]