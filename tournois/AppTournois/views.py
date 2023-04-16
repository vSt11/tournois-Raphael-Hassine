from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Tournoi, Poule

def tournois(request):
    tournois = Tournoi.objects.all()
    context = {
        'tournois': tournois,
    }
    return render(request, 'tournois/tournois.html', context)

def tournoi(request, tournoi_id):
    tournoi = Tournoi.objects.get(id=tournoi_id)
    poules = Poule.objects.filter(tournoi=tournoi)
    context = {'tournoi': tournoi, 'poules': poules}
    return render(request, 'tournois/tournoi.html', context)

def poule(request, poule_id):
    poule = Poule.objects.get(id=poule_id)
    context = {
        'poule': poule,
        'matches': poule.get_matches(),
        'standings': poule.get_standings(),
    }
    return render(request, 'tournois/detail_poule.html', context)