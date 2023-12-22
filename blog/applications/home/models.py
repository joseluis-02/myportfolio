#Apps de django
from django.db import models

# Apps de terceros
from model_utils.models import TimeStampedModel

# Modelo de home para pagina principal
class Home(TimeStampedModel):
    title = models.CharField(
        'Título',
        max_length=50
    )
    description = models.TextField()
    about_title = models.CharField(
        'Título nosotros',
        max_length=70
    )
    contact_email = models.CharField(
        'Email de contacto',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Celular de contacto',
        max_length=20
    )

    class Meta:
        verbose_name = 'Página principal'
        verbose_name_plural = 'Página principal'
    def __str__(self) -> str:
        return f"{self.id} - {self.title} - {self.description}"
# Modelo para suscriptores
class Suscribers(TimeStampedModel):
    email = models.EmailField()
    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural= 'Suscriptores'
    def __str__(self) -> str:
        return f"{self.id} - {self.email}"
# Modelo para contactos
class Contact(TimeStampedModel):
    full_name = models.CharField(
        "Nombres",
        max_length=70
    )
    email = models.EmailField()
    messagge=models.TextField()
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
    def __str__(self) -> str:
        return f"{self.id} - {self.full_name} - {self.email} - {self.messagge}"
