from django.db import models

from django.contrib.auth.models import User
group = (('A+','A+'),('A-','A-'),('A','A'),('B+','B+'),('B-','B-'),('B','B'),('O+','O+'),('O-','O-'),('O','O'))
genre = (('Homme','Homme'),('Femme','Femme'))
commune = (('Muha','Muha'),('Ntahangwa','Ntahangwa'),('Mukaza','Mukaza'))
class Doneur(models.Model):
    nom=models.CharField(max_length=250)
    bloodgroup=models.CharField(max_length = 15,choices= group)
    genre = models.CharField(max_length = 15,choices= genre)
    age = models.IntegerField()
    commune = models.CharField(max_length = 15,choices= commune)
    zone = models.CharField(max_length=100)
    Tel = models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.name


class Categorie(models.Model):
	nom = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.nom

nom = (('A+','A+'),('A-','A-'),('A','A'),('B+','B+'),('B-','B-'),('B','B'),('O+','O+'),('O-','O-'),('O','O'))

class Produit(models.Model):
	nature_produit = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=False)
	nom_produit = models.CharField(max_length = 15,choices= nom)
	date_donation = models.DateTimeField(auto_now_add=False)

	def __str__(self):
		return self.nom_produit

	class Meta:
		unique_together = ('nature_produit','nom_produit','date_donation')

class Stock(models.Model):
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True)
	nom_produit = models.CharField(max_length = 15,choices= nom)
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
	date_donation = models.DateTimeField(auto_now_add=False)

	

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
	date_donation = models.DateTimeField(auto_now_add=False)

	