
from django.urls import path
from .views import *
 #To use url in templates

urlpatterns = [
    
    
    path('create/',ProduitCreateView.as_view(), name='create'),
    #path('update/<int:pk>',views.SchoolUpdateView.as_view(),name = 'update'),
    #path('delete/<int:pk>',views.SchoolDeleteView.as_view(),name = 'delete'),
]