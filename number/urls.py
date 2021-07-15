from django.urls import path
from .views import views, index, si

urlpatterns = [
    path('', index.index),
    path('número', views.convert_num),
    path('comprimento', si.unit_lenght)
    
]