from django import forms

class ListadoTareasForms (forms.Form):
    text = forms.CharField(max_length=45, 
        widget=forms.TextInput(
            attrs = {'class': 'form-control', 'placeholder': 'Ingresar una tarea, ejemplo: limpiar', 
                     'aria-label': 'Tareas', 'aria-describeby': 'add-btn'})
        )