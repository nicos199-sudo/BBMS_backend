from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['categorie', 'nom_produit', 'quantite']

	def clean_categorie(self):
		categorie = self.cleaned_data.get('categorie')
		if not categorie:
			raise forms.ValidationError('veillez remplir ce chanp!!')

		#for instance in Stock.objects.all():
			#if instance.categorie == categorie:
				#raise forms.ValidationError(str(categorie) + ' is already created')
		
		return categorie


	def clean_nom_produit(self):
		nom_produit = self.cleaned_data.get('nom_produit')
		if not nom_produit:
			raise forms.ValidationError('veillez remplir ce chanp!!')
		for instance in Stock.objects.all():
			if instance.nom_produit == nom_produit:
				raise forms.ValidationError(str(nom_produit) + ' deja cree!')
		return nom_produit

class StockSearchForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required=False)
	class Meta:
		model = Stock
		fields = ['categorie', 'nom_produit']

class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['categorie', 'nom_produit', 'quantite']



class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['quantite_servie', 'servie_a']


class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['quantite_recue', 'recue_par']


class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['changer_niveau_stock']
