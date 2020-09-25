from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def spurs(request):
    return render(request, 'Teams/Spurs/spurs.html')

def liverpool(request):
    return render(request, 'Teams/Liverpool/liverpool.html')

def liverpoolVChelsea(request):
    return render(request, 'Teams/Liverpool/Matches/LiverpoolVChelsea.html')

def spursVSoton(request):
    return render(request, 'Teams/Spurs/Matches/SpursVSoton.html')

def spursVShkendija(request):
    return render(request, 'Teams/Spurs/Matches/Shkendija.html')

def home(request):
    return render(request, 'Landing/home.html')

def teams(request):
    return render(request, 'Landing/teams.html')

def players(request):
    return render(request, 'Landing/players.html')

def skriniar(request):
    return render(request, 'Teams/Spurs/Players/skriniar.html')
