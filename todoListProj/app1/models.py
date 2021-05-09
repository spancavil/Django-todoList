from django.db import models

# Create your models here.

#Definimos como se guardarán los datos en mi db.
class ListaQueHaceres(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text