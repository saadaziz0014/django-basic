from django.shortcuts import render
from .models import Shirt
from django.shortcuts import get_object_or_404
# Create your views here.

def Home(request):
    return render(request, 'saad/saad.html')

def Shirts(request):
    shirts = Shirt.objects.all()
    return render(request, 'saad/shirts.html', {'shirts':shirts})

def Shirt(request, shirt_id):
    shirt = get_object_or_404(Shirt, pk=shirt_id)
    return render(request, 'saad/shirt.html', {'shirt':shirt})