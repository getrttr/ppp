from django.shortcuts import render
from products.models import Product,ProductCategory

def index(request):
    return render(request, 'products/index.html')

def email(request):
    return render(request, 'products/email_verification.html')

def login(request):
    return render(request, 'products/login.html')

def profile(request):
    return render(request, 'products/profile.html')

def register(request):
    return render(request, 'products/register.html')

def products(request):
    context = {
        'categories': ProductCategory.objects.all(),
        'products' : Product.objects.all(),
    }
    return render(request, 'products/products.html', context)