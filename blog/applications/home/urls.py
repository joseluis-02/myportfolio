#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ),
    path(
        'add-suscriptors', 
        views.SuscribersCreateView.as_view(),
        name='add-suscriptors',
    ),
    path(
        'add-contact', 
        views.ContactCreateView.as_view(),
        name='add-contact',
    ),
]