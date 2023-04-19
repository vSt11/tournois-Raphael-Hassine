from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Tournoi, Poule, Commentaire, Match
from django.contrib.auth.decorators import login_required
from .forms import CommentaireForm
from django.template.loader import render_to_string

@login_required
def modifier_commentaire(request, Commentaire_id):
    commentaire = get_object_or_404(Commentaire, id=Commentaire_id)

    if request.method == 'POST':
        form = CommentaireForm(request.POST)

        if form.is_valid():
            commentaire.contenu = form.cleaned_data['contenu']
            commentaire.save()
            return HttpResponseRedirect(reverse('afficher_match', args=(commentaire.match.id,)))
    else:
        form = CommentaireForm(initial={'contenu': commentaire.contenu, 'match_id': commentaire.match.id})

    context = {
        'form': form,
        'commentaire': commentaire,
    }

    return render(request, 'tournois/modifier_commentaire.html', context)
                  
@login_required
def commenter(request, match_id):
    print("test1")
    match = get_object_or_404(Match, id=match_id)
    form = CommentaireForm(initial={'auteur': request.user, 'match_id': match.id})
    if request.method == 'POST':
        print("test2")
        form = CommentaireForm(request.POST)
        if form.is_valid():
            print("test3")
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user
            commentaire.match = match
            commentaire.save()
        return redirect(reverse('commenter', kwargs={'match_id': match_id}))
    return render(request, 'tournois/match.html', {'form': form, 'match_id': match.id, 'match': match})

# @login_required
# def commenter(request, match_id):
#     print("True")
#     match = get_object_or_404(Match, id=match_id)
#     if request.method == 'POST':
#         form = CommentaireForm(request.POST)
#         print("form")
#         if form.is_valid():
#             print("isvalid")
#             commentaire = form.save(commit=False)
#             print(commentaire)
#             commentaire.auteur = request.user
#             commentaire.match = match
#             commentaire.save()
#             print("save")
#             # Générer le HTML pour le nouveau commentaire et le renvoyer au client
#             comment_html = render_to_string('tournois/commenter.html', {'commentaire': commentaire})
#             return JsonResponse({'html': comment_html})
#     else:
#         form = CommentaireForm(initial={'auteur': request.user, 'match_id': match})
#     return render(request, 'tournois/commenter.html', {'form': form})



# @login_required
# def commenter(request, match_id):
#     match = get_object_or_404(Match, id=match_id)
#     if request.method == 'POST':
#         form = CommentaireForm(request.POST)
#         if form.is_valid():
#             commentaire = form.save(commit=False)
#             commentaire.auteur = request.user
#             commentaire.match = match
#             commentaire.save()
#             return redirect('tournois/match/<int:match_id>', match_id=match.id)
#     else:
#         form = CommentaireForm()
#     context = {'match': match, 'form': form}
#     return render(request, 'tournois/commenter.html', context)

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
