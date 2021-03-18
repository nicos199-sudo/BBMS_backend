from django.db import models
from django.contrib.auth.models import User
#from ..Accounts.models import Employe,Visiteur
decision = (('1','Accepter'),('0','Refuse'))
sexe = (("H", 'Homme'), ("F", "Femme"))

# Create your models here.
class Service(models.Model):
	nom = models.CharField(max_length = 30)

	def __str__(self):
		return f"{self.nom}"

	class Meta:
		ordering = ["nom"]

class FicheDemande(models.Model):
	service_Demandeur = models.ForeignKey(Service,on_delete=models.CASCADE)
	nombre_Poche = models.IntegerField()
	docteur =models.CharField(max_length = 20)
	nomReceveur = models.CharField(max_length = 40)
	age = models.PositiveIntegerField()
	genre = models.CharField(max_length = 20,choices=sexe )
	lieu_Naissance = models.CharField(max_length = 20)
	motif_Transfusion = models.TextField()
	dateFiche = models.DateField(auto_now_add = True)
	status = models.CharField(max_length = 10,choices= decision,default='En Attente')
	visiteur = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.visiteur}   {self.nomHopital}"

	#class Meta:
		#unique_together = ('visiteur', 'dateFiche',)


class FicheRecquisition(models.Model):
	quantiservie = models.CharField(max_length= 15)
	dateFiche = models.DateField()
	#demande = models.ForeignKey(FicheDemande, on_delete= models.CASCADE ,default=1)
	gestionnaire = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.quantiservie}  {self.demande.service_Demandeur}"


class BonExpedetion(models.Model):
	quantiteExpedier =models.FloatField()
	prixUnit =models.PositiveIntegerField()
	observation =models.TextField(max_length = 2000)
	fiche_recqui = models.ForeignKey(FicheRecquisition, on_delete = models.CASCADE,default=1)
	dateBon = models.DateField()
	gestionnaire = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.quantiteExpedier}--{self.observation}"