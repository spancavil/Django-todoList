from django.shortcuts import render
# from .models import ListaQueHaceres

# Create your views here.
def index(request):
    # todo_items = ListaQueHaceres.objects.order_by('id')
    # context = {'todo_items' : todo_items}
    return render(request,'app1/index.html')