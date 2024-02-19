from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ecomerce_site/index.html')

def about(request):
    return render(request, 'ecomerce_site/about.html')