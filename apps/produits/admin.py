from django.contrib import admin
from .models import Stock, Categorie, Produit, Doneur
from .forms import StockCreateForm


# Register your models here.
class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['categorie', 'nom_produit', 'quantite','date_donation']
   form = StockCreateForm
   list_filter = ['categorie']
   search_fields = ['categorie', 'nom_produit']

admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Doneur)