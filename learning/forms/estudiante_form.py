from ..models import Estudiante
from django import forms

class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante
        fields = ['nombre', 'email']
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo electrónico',
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            'email': forms.EmailInput(attrs={"class" : "form-control"})
        }




