from django.contrib import admin

from .models import ListadoTareas

# Register your models here.
# Necesitamos que nuestro modelo sea accesible al panel del admin (de momento)
admin.site.register(ListadoTareas)
