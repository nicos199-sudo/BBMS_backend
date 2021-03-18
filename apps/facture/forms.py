from django import forms
from .models import *

class FactureForm(forms.ModelForm):
	class Meta:
		model = Facture
		fields = '__all__'
		exclude = ['gestionnaire','dateFacture',]

"""class ProduitCommandeForm(forms.ModelForm):
	class Meta:
		model = ProduitCommande
		fields = '__all__'
		exclude = ['gestionnaire',]"""

class FacturationForm(forms.ModelForm):
	class Meta:
		model = Facturation
		fields = '__all__'
		exclude = ['gestionnaire','dateFacturation',]