from ..models import Curso, Instructor
from django import forms

class CursoForm(forms.ModelForm):

    instructor = forms.ModelChoiceField(
        queryset=Instructor.objects.all(),
        required=False,
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
            'nombre': forms.TextInput(attrs={"class" : "form-control"}),
            'descripcion': forms.Textarea(attrs={"class" : "d-flex form-control"}),
            'precio': forms.NumberInput(attrs={"class" : "form-control"}),
            'fecha_publicacion': forms.NumberInput(attrs={'type':'date', "class" : "form-control"}),
        }

