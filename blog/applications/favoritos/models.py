# Apps de django
from django.db import models
from django.conf import settings

#Apps de terceros
from model_utils.models import TimeStampedModel

# Models extra
from applications.entrada.models import Entry

#Managers
from .managers import (
    FavoritesManager
)

# Model de favoritos
class Favorites(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name= 'user_favorites',
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_fovorites',
        on_delete=models.CASCADE,
    )

    #Uniendo a managers
    objects=FavoritesManager()

    class Meta:
        unique_together=('user','entry')
        verbose_name = 'Entrada fovorita'
        verbose_name_plural='Entradas fovoritas'
    
    def __str__(self) -> str:
        return f"{self.id} - {self.user } - {self.entry}"
