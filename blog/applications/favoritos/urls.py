#Django
from django.urls import path
from . import views

app_name = "favoritos_app"

urlpatterns = [
    path(
        'perfil', 
        views.UserPageListView.as_view(),
        name='perfil',
        
    ),
    path(
        'add-favorito/<pk>', 
        views.AddFovoritosView.as_view(),
        name='add-favorito',
    ),
    path(
        'delete-favorito/<pk>', 
        views.FavoritosDeleteView.as_view(),
        name='delete-favorito',
    ),
]