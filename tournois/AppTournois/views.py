from django.shortcuts import render
from django.http import HttpResponse
from .models import Tournoi

def index(request):
    return HttpResponse("Hello, world. You're at the tournament index.")

def tournois(request):
    tournois = Tournoi.objects.all()
    context = {
        'tournois': tournois,
    }
    return render(request, 'tournois/tournois.html', context)