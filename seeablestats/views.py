from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ndombele(request):
    return render(request, 'vis/ndombele.html')

def spurs(request):
    return render(request, 'spurs.html')

def soton(request):
    return render(request, 'vis/soton.html')

def home(request):
    return render(request, 'home.html')

def teams(request):
    return render(request, 'teams.html')
