from django.db import models

# Create your models here.
# Los modelos definen como se guardarán todos los datos del proyecto en la base de datos.
# Una vez generado el modelo está en formato python y hay que transpilarlo haciendo un makemigrations (para que lo traspile a un
# lenguaje SQL) y posteriormente aplicar dichos cambios a la db definita del projecto (crea una tabla respectiva)
# haciendo un migrate.

class ListadoTareas(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text