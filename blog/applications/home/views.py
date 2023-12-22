import datetime
from typing import Any
# Django
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)
#Models
from applications.entrada.models import Entry
from applications.home.models import Home
#Forms
from .forms import SuscribersForm,ContactForm

#Views
class HomePageView(TemplateView):
    template_name = "home/index.html"
    #Funciones
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        contex = super(HomePageView,self).get_context_data(**kwargs)
        #Cargamos los datos al home
        contex['home'] = Home.objects.latest('created')
        #contexto para la portada
        contex['portada'] = Entry.objects.entrada_en_portada()
        #contexto para los artículos en home
        contex['entradas_home'] = Entry.objects.entradas_en_home()
        #contexto entradas recientes
        contex['entradas_recientes'] = Entry.objects.entradas_recientes()

        #COntexto de envio de formulario al template
        contex['form_suscribirse'] = SuscribersForm
        return contex

class SuscribersCreateView(CreateView):
    form_class=SuscribersForm
    success_url='.'
class ContactCreateView(CreateView):
    form_class=ContactForm
    success_url='.'


