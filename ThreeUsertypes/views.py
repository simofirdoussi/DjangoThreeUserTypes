from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, 'ThreeUsertypes/register.html')

def login(request):
    return render(request, 'ThreeUsertypes/login.html')
