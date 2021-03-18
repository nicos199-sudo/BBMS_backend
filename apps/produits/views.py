from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ( 
	View,
	TemplateView, 
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView

	)
from apps.produits.models import *
# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "base.html",context)

class ProduitCreateView(CreateView):
    fields = ('nature_produit','nom_produit')
    model = Produit
