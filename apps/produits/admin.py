from django.contrib import admin
from .models import Stock, Categorie, Produit
from .forms import StockCreateForm


# Register your models here.
class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['categorie', 'nom_produit', 'quantite']
   form = StockCreateForm
   list_filter = ['categorie']
   search_fields = ['categorie', 'nom_produit']

admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Categorie)
admin.site.register(Produit)