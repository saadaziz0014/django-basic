from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return HttpResponse("Hello, world. You're at the basic index.")


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contacts/contact.html')