from django.urls import path
from . import views

app_name = 'career'
urlpatterns = [
    path('', views.career, name='career'),
]

