from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields= [
            'nombre',
            'apellido',
            'tipodocumento',
            'documento',
            'lugarresidencia',
            'fechanacimiento',
            'email',
            'telefono',
            'usuario',
            'password',
        ]