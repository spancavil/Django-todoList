from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #Este pattern incluido en nuestro proyecto toma el path home y por cada request le envía de views, el método index (que básicamente es el que renderiza la pág)
    path('add', views.addTarea, name='add'), # Añadimos el path add y la dirección a dónde apunta
    path('completada/<tarea_id>', views.tareaCompletada , name='completada'), #Le pasamos tarea id al método tareaCompletada de las views
    path('borrarCompletada', views.borrarCompletada, name= 'borrarCompletada'),
    path('borrarTodo', views.borrarTodo, name = 'borrarTodo')
]