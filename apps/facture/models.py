from django.db import models

# Create your models here.
from ..fiches.models import BonExpedetion
from django.contrib.auth.models import User

# Create your models here.
class Facture(models.Model):
	idFacture = models.IntegerField(primary_key = True)
	montant = models.FloatField()
	dateFacture = models.DateField(auto_now_add= True)
	gestionnaire = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.idFacture}--{self.montant}"

	#def get_montant(self):
		#prix = 

class Facturation(models.Model):
	bonExpedetion = models.ForeignKey(BonExpedetion, on_delete = models.CASCADE)
	facture = models.ForeignKey(Facture, on_delete = models.CASCADE)
	montantPaye = models.PositiveIntegerField()
	dateFacturation = models.DateField(auto_now_add = True)
	gestionnaire = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return f"{self.Facture.idFacture}--{self.montantPaye}"