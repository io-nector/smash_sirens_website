from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'ecomerce_site/index.html')

def about(request):
    return render(request, 'ecomerce_site/about.html')

def merch(request):
    products = Product.objects.all()
    return render(request, 'ecomerce_site/merch.html', 
        {
            'products': products
    })


    