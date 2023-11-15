from ..models import Curso, Instructor
from django import forms

class CursoForm(forms.ModelForm):

    instructor = forms.ModelChoiceField(
        queryset=Instructor.objects.all(),
        blank=True,
        empty_label="Seleccione el profesor",
        widget=forms.Select(
            attrs={
                "class": 'form-control'
            }
        )
    )

    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'precio', 'fecha_publicacion', 'instructor']
        labels = {
            'nombre': 'Nombre del curso',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'fecha_publicacion': 'Fecha de publicación',
            'instructor': 'Instructor'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre del curso'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Ingrese la descripción'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio'}),
            'fecha_publicacion': forms.NumberInput(attrs={'type':'date', 'placeholder': 'Ingrese la fecha'}),
        }

