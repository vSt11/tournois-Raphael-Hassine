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

def detail_poule(request, poule_id):
    poule = get_object_or_404(Poule, pk=poule_id)
    context = {
        'poule': poule,
    }
    return render(request, 'tournois/detail_poule.html', context)