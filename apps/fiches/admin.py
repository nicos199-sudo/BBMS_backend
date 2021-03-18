from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(BonExpedetion)
admin.site.register(FicheRecquisition)
admin.site.register(FicheDemande)
admin.site.register(Service)