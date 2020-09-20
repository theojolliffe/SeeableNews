from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ndombele(request):
    return render(request, 'vis/ndombele.html')

def soton(request):
    return render(request, 'vis/soton.html')
