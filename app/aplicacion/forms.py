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
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'tipodocumento': forms.Select(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'lugarresidencia': forms.Select(attrs={'class': 'form-control'}),
            'fechanacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pass1'}),
        }