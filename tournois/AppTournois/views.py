from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Tournoi, Poule, commentaire, Match
from django.contrib.auth.decorators import login_required
from .forms import CommentaireForm


@login_required
def commenter(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user
            commentaire.match = match
            commentaire.save()
            return redirect('tournois/match', match_id=match.id)
    else:
        form = CommentaireForm()
    context = {'match': match, 'form': form}
    return render(request, 'tournois/commenter.html', context)

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
    poule = Poule.objects.get(pk=poule_id)
    context = {
        'poule': poule,
        'matches': poule.get_matches(),
        'standings': poule.get_standings(),
    }
    return render(request, 'tournois/detail_poule.html', context)


def match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    context = {'match': match}
    return render(request, 'tournois/match.html', context)


