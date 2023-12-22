#Django
from typing import Any
from django.http import HttpResponseRedirect
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View,
    ListView,
    DeleteView,
)
#Models 
from .models import (
    Favorites,
    Entry
)
# Views

class UserPageListView(LoginRequiredMixin,ListView):
    template_name = "favoritos/perfil.html"
    context_object_name="entradas_user"
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self) -> QuerySet[Any]:
        return Favorites.objects.entradas_user(self.request.user)


class AddFovoritosView(LoginRequiredMixin,View):
    #Esta vista necesita usuario logueado
    login_url = reverse_lazy('users_app:user-login')

    def post(self,request,*args, **kwargs):
        #recuperar usuario
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        #Registramos el favorito
        try:
            Favorites.objects.create(
                user=usuario,
                entry=entrada,
            )
        finally:
            return HttpResponseRedirect(
                reverse(
                    'favoritos_app:perfil',
                )
            )
            

class FavoritosDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')
