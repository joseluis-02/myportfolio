# Django
from django.contrib import admin
#Models
from .models import *
# Register models
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Entry)
