#Python
from datetime import (
    datetime,
    timedelta,
)
# Apps de django
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

# Apps de teceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

#Managers
from .managers import *

# Modelo categoria
class Category(TimeStampedModel):
    short_name = models.CharField(
        'Nombre corto',
        max_length=15,
        unique=True
    )
    name = models.CharField(
        'Nombre',
        max_length=30
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return f"{self.id} - {self.name} - {self.short_name}"

# Model Tags  
class Tag(TimeStampedModel):
    name = models.CharField(
        'Nombre',
        max_length=30
    )

    class Meta:
        verbose_name='Etiqueta'
        verbose_name_plural='Tags'
    
    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

# Modelo entrada 
class Entry(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Título',
        max_length=200
    )
    resume = models.TextField(
        'Resumen'
    )
    content = RichTextUploadingField('Contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Imagen',
        upload_to='Entry',
    )
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False,max_length=300)

    #Conectando con el manager
    objects=EntryManager()

    class Meta:
        verbose_name='Entrada'
        verbose_name_plural='Entradas'
    
    def __str__(self) -> str:
        return f"{self.id} - {self.user} - {self.category} - {self.title} - {self.resume}"
    
    def get_absolute_url(self):
        return reverse_lazy(
            'entrada_app:entry-detail',
            kwargs={
                'slug': self.slug
            }
        )
    
    def save(self, *args,**kwargs):
        # Hacer que tenga un identificador unico
        # Usar tiempo
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconts = int(total_time.total_seconds())
        slug_unique = f"{self.title}-{seconts}"
        self.slug = slugify(slug_unique)
        #sobreescribir el metodo super 
        super(Entry,self).save(*args,**kwargs)