from django.db import models


class Categorie(models.Model):
	nom = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.nom

class Produit(models.Model):
	nature_produit = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=False)
	nom_produit = models.CharField(max_length=200)
	date_donation = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nom_produit

class Stock(models.Model):
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True)
	nom_produit = models.CharField(max_length=50, blank=True, null=True)
	quantite = models.IntegerField(default='0', blank=False, null=True)
	quantite_recue = models.IntegerField(default='0', blank=True, null=True)
	recue_par = models.CharField(max_length=50, blank=True, null=True)
	quantite_servie = models.IntegerField(default='0', blank=True, null=True)
	servie_par = models.CharField(max_length=50, blank=True, null=True)
	servie_a = models.CharField(max_length=50, blank=True, null=True)
	tel = models.CharField(max_length=50, blank=True, null=True)
	creer_par = models.CharField(max_length=50, blank=True, null=True)
	changer_niveau_stock = models.IntegerField(default='0', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	dernier_misajour = models.DateTimeField(auto_now_add=False, auto_now=True)

	

	def __str__(self):
		return self.nom_produit 

class StockHistory(models.Model):
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True)
	nom_produit = models.CharField(max_length=50, blank=True, null=True)
	quantite = models.IntegerField(default='0', blank=False, null=True)
	quantite_recue = models.IntegerField(default='0', blank=True, null=True)
	recue_par = models.CharField(max_length=50, blank=True, null=True)
	quantite_servie = models.IntegerField(default='0', blank=True, null=True)
	servie_par = models.CharField(max_length=50, blank=True, null=True)
	servie_a = models.CharField(max_length=50, blank=True, null=True)
	tel = models.CharField(max_length=50, blank=True, null=True)
	creer_par = models.CharField(max_length=50, blank=True, null=True)
	changer_niveau_stock = models.IntegerField(default='0', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	

	