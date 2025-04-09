"""
URL configuration for GestionQuartier project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from CandyImmo import views

from django.urls import path
from CandyImmo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.initial, name='initial'),  # Page d'accueil initiale
    path('accueil/', views.accueil, name='accueil'),  # Page pour créer un quartier
    path('maison/', views.maison, name='maison'),  # Page pour créer une maison
]