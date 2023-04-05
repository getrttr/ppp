from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def email(request):
    return render(request, 'products/email_verification.html')

def login(request):
    return render(request, 'products/login.html')

def profile(request):
    return render(request, 'products/profile.html')

def register(request):
    return render(request, 'products/register.html')
