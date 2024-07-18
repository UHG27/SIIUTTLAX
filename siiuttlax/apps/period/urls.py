from django.urls import path
from . import views

urlpatterns = [
    path('', views.period_list, name='period_list'),
    
]
