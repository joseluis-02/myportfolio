#Django
from typing import Any
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
# Models
from .models import Entry, Category
# Views
class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name='entradas'
    paginate_by=2
    #Creando contexto
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(EntryListView,self).get_context_data(**kwargs)
        context['categorias']=Category.objects.all()
        return context
    #Funciones
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        categoria = self.request.GET.get('categoria', '')
        #Consulta de busqueda
        result = Entry.objects.buscar_entrada(kword,categoria)
        return result


class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"
