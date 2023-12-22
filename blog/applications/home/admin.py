# Apps de django 
from django.contrib import admin

# Models externos
from .models import *

# Register models.
admin.site.register(Home)
admin.site.register(Suscribers)
admin.site.register(Contact)
