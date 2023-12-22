#Django
from django.db import models


#Managers
class EntryManager(models.Manager):
    #Devuelve el ultimo articulo publicado
    def entrada_en_portada(self):
        return self.filter(
            public=True,
            portada=True,
        ).order_by('-created').first()
    #Devuelve las ultimas 4 entradas en home
    def entradas_en_home(self):
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]
    #Entradas las ultimas 6 recientes
    def entradas_recientes(self):
        return self.filter(
            public=True,
        ).order_by('-created')[:6]
    #Buscar por palabra clave y una categoria
    def buscar_entrada(self,kword,categoria):
        # Procedimiento para buscar
        if len(categoria) > 0:
            return self.filter(
                category__short_name =categoria,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')
