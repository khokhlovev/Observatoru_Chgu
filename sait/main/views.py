from django.shortcuts import render
from .models import Task


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def catalogue(request):
    tasks =Task.objects.all()
    return render(request, 'main/catalogue.html', {'title':'Эксурурсии', 'tasks': tasks })

def phone(request):
    return render(request, 'main/phone.html')

def login(request):
    return render(request, 'main/login.html')