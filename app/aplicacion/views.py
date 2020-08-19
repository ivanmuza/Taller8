from django.shortcuts import render, redirect
from .models import *
from .forms import PersonaForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def home(request):
    return render(request,'index.html')

class CreatePersona(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'aplicacion/crear_persona.html'
    success_url = reverse_lazy('listar_persona')

class ListPersona(ListView):
    model = Persona
    template_name = 'aplicacion/listar_persona.html'

class UpdatePersona(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'aplicacion/editar_persona.html'
    success_url = reverse_lazy('listar_persona')

class DeletePersona(DeleteView):
    model = Persona
    template_name = 'aplicacion/eliminar_persona.html'
    success_url = reverse_lazy('listar_persona')
