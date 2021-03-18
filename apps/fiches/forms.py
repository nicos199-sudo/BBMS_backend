from django import forms
from .models import *

class bonExpForm(forms.ModelForm):
	class Meta:
		model = BonExpedetion
		fields = '__all__'
		exclude = ['gestionnaire','dateBon',]
		
class FicheRecForm(forms.ModelForm):
	class Meta:
		model = FicheRecquisition
		fields = '__all__'
		exclude = ['gestionnaire',]

class FicheDemaForm(forms.ModelForm):
	class Meta:
		model = FicheDemande
		fields = '__all__'
		exclude = ['visiteur','dateFiche','status']