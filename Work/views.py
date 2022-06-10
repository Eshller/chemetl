from django.shortcuts import render
from .models import Product , Material , Contact

AllProducts = Product.objects.all()
AllMaterials = Material.objects.all()
AllContact = Contact.objects.all()
context = {"Products" : AllProducts , "Material" : AllMaterials , "ContactList" : AllContact}

# Create your views here.
def index(request):
    return render(request , 'Work/index.html' ,context)

def about(request , id):
    ProductF = Product.objects.get(pk=id)
    return render(request , "Work/AboutProduct.html" , {"Product" : ProductF})

def comp(request, id):
    MaterialF = Material.objects.get(pk=id)
    return render(request , "Work/AboutMat.html" , {"Material" : MaterialF})
