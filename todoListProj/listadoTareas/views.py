from django.shortcuts import render

from .models import ListadoTareas

# Create your views here.

def index(request):
    listado_items = ListadoTareas.objects.order_by('id') #Le pasamos el listado de items a través de la importación del modelo correspondiente.
    context = {'listado_items': listado_items} #definimos un diccionario cuyo contenido son los objetos de mi modelo
    return render(request, 'listadoTareas/index.html', context) #renderizamos el site (listadoTareas/index está dentro de templates) y además le pasamos el context que definimos