from django.shortcuts import render, redirect

from .models import ListadoTareas
from .forms import ListadoTareasForms

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    listado_items = ListadoTareas.objects.order_by('id') #Le pasamos el listado de items a través de la importación del modelo correspondiente.
    form = ListadoTareasForms() # Declaramos el form de la clase ListadoTareasForms que se importo desde el archivo forms.py

    context = {'listado_items': listado_items, 'form': form} #definimos un diccionario cuyo contenido son los objetos de mi modelo

    return render(request, 'listadoTareas/index.html', context) #renderizamos el site (listadoTareas/index está dentro de templates) y además le pasamos el context que definimos

@require_POST #el require_POST restringe el acceso a addTarea a sólo métodos post.
def addTarea(request):
    form = ListadoTareasForms(request.POST)
    print(request.POST['text']) # Es un test para ver si el form me está tomando los datos.

    if form.is_valid():
        nueva_tarea = ListadoTareas(text = request.POST['text']) #Guardamos el dato según el model. Sacamos los datos del POST que se hizo desde el form.
        #Le ponemos text porque así lo definimos en models.
        nueva_tarea.save() # Loa guardamos en la db

    return redirect('index') # Una vez que definimos el redirect, tenemos que agregar un URL pattern
    # Se redirige a index y renderiza nuevamente todos los datos (con los datos de la db guardados también)

def tareaCompletada (request, tarea_id):
    tarea = ListadoTareas.objects.get(pk=tarea_id) #Captamos de nuestro ListadoTareas los objetos cuya key coincidan con el id que le pasaron por parametro.
    print (tarea, tarea_id)
    tarea.completed = True # Lo setteamos a true
    tarea.save()            #Lo guardamos finalmente en la db.
    return redirect('index')

def borrarCompletada (request):
    ListadoTareas.objects.filter(completed__exact= True).delete()
    return redirect('index')

def borrarTodo (request):
    ListadoTareas.objects.all().delete()
    return redirect ('index')