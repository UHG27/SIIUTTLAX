"""
URL configuration for siiuttlax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from apps.home import views as home_views

urlpatterns = [
    path('', home_views.home, name='home'),  # Página de inicio
    path('admin/', admin.site.urls),  # Administración de Django
    path('registration/login/', LoginView.as_view(template_name='login.html'), name='login'),  # Login personalizado
    path('registration/', include('django.contrib.auth.urls')),  # URLs de autenticación (logout, password change, etc.)
    path('academy/', include('apps.academy.urls')),  # URLs de la app "academy"
    path('career/', include('apps.career.urls')),  # URLs de la app "career"
    path('period/', include('apps.period.urls')),  # URLs de la app "period"
]