from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('surface', 'ville', 'prix_mettre', 'variation', 'predictions')

admin.site.register(Data, DataAdmin)