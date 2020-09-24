from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ndombele(request):
    return render(request, 'vis/ndombele.html')

def spurs(request):
    return render(request, 'spurs.html')

def liverpool(request):
    return render(request, 'liverpool.html')

def liverpoolVChelsea(request):
    return render(request, 'vis/LiverpoolVChelsea.html')

def spursVSoton(request):
    return render(request, 'vis/SpursVSoton.html')

def home(request):
    return render(request, 'home.html')

def teams(request):
    return render(request, 'teams.html')

def players(request):
    return render(request, 'players.html')

def skriniar(request):
    return render(request, 'skriniar.html')
