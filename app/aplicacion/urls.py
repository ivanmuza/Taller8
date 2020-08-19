from django.conf.urls import url
from .views import *
from .forms import PersonaForm

urlpatterns = [
    url(r'^$',home,name= "index"),
    url(r'^crear_persona/',CreatePersona.as_view(), name= "crear_persona"),
    url(r'^listar_persona/',ListPersona.as_view(), name= "listar_persona"),
    url(r'^editar_persona/(?P<pk>\d+)/$',UpdatePersona.as_view(), name= "editar_persona"),
    url(r'^eliminar_persona/(?P<pk>\d+)/$',DeletePersona.as_view(), name= "eliminar_persona"),
]