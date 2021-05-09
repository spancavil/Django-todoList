from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') #Este pattern incluido en nuestro proyecto toma el path home y por cada request le envía de views, el método index (que básicamente es el que renderiza la pág)
]