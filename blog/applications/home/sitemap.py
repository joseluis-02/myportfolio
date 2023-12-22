#Python
from datetime import timedelta, datetime
#Django
from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy
#Models
from applications.entrada.models import (
    Entry
)
#SiteMaps
class EntrySitemap(Sitemap):
    changedfreq = 'weekly'
    priority=0.8
    protocol='https'
    #funciones
    def items(self):
        return Entry.objects.filter(public=True)
    def lastmod(self,obj):
        return obj.created
class Sitemap(Sitemap):
    protocol='https'

    #Funciones
    def __init__(self,names):
        self.names = names
    def items(self):
        return self.names
    def changedfreq(self,obj):
        return 'weekly'
    def lastmod(self,obj):
        return datetime.now()
    def location(self,obj):
        return reverse_lazy(obj)

