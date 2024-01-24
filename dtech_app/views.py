from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .models import Webpage
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    employees = Employee.objects.all().order_by('date')
    return render(request, 'main/about.html', {'employees': employees})

def contact(request):
    webpages = Webpage.objects.all()
    return render(request, 'main/contact.html', {'webpages': webpages}) 
    