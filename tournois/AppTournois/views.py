from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Tournoi, Poule, Commentaire, Match
from django.contrib.auth.decorators import login_required
from .forms import CommentaireForm
from django.template.loader import render_to_string


@login_required
def modifier_commentaire(request, Commentaire_id):
    # Récupérer le commentaire en fonction de l'ID
    commentaire = get_object_or_404(Commentaire, id=Commentaire_id)

    if request.method == 'POST':
        # Si la requête est de type POST, créer une instance du formulaire et le remplir avec les données de la requête
        form = CommentaireForm(request.POST)

        if form.is_valid():
            # Si le formulaire est valide, mettre à jour le contenu du commentaire avec les données du formulaire
            commentaire.contenu = form.cleaned_data['contenu']
            commentaire.save()
            # Rediriger l'utilisateur vers la page de commentaires pour le match correspondant
            return HttpResponseRedirect(reverse('commenter', args=(commentaire.match.id,)))
    else:
        # Si la requête n'est pas de type POST, créer une instance du formulaire avec les données du commentaire
        form = CommentaireForm(
            initial={'contenu': commentaire.contenu, 'match_id': commentaire.match.id})

    # Passer le formulaire et le commentaire à la vue
    context = {
        'form': form,
        'commentaire': commentaire,
    }

    # Afficher le template pour modifier un commentaire
    return render(request, 'tournois/modifier_commentaire.html', context)


@login_required
def commenter(request, match_id):
    # Récupération de l'objet Match correspondant à l'ID fourni
    match = get_object_or_404(Match, id=match_id)
    # Initialisation du formulaire Commentaire avec l'utilisateur connecté et l'ID du match courant
    form = CommentaireForm(
        initial={'auteur': request.user, 'match_id': match.id})
    # Si le formulaire est soumis via une requête POST
    if request.method == 'POST':
        # On instancie un nouveau formulaire Commentaire avec les données de la requête POST
        form = CommentaireForm(request.POST)
        # Si le formulaire est valide
        if form.is_valid():
            # On crée un nouvel objet Commentaire avec les données du formulaire, sans l'enregistrer en base de données
            commentaire = form.save(commit=False)
            # On associe l'utilisateur connecté à l'objet Commentaire
            commentaire.auteur = request.user
            # On associe l'objet Match courant à l'objet Commentaire
            commentaire.match = match
            # On enregistre l'objet Commentaire en base de données
            commentaire.save()
            # On redirige l'utilisateur vers la page de commentaires du match courant
            return redirect(reverse('commenter', kwargs={'match_id': match_id}))
    # On affiche le formulaire Commentaire et la liste des commentaires déjà enregistrés pour le match courant
    return render(request, 'tournois/match.html', {'form': form, 'match_id': match.id, 'match': match})


def tournois(request):
    # Récupération de tous les objets Tournoi enregistrés en base de données
    tournois = Tournoi.objects.all()
    context = {
        'tournois': tournois, }
    # Affichage de la page listant tous les tournois
    return render(request, 'tournois/tournois.html', context)


def tournoi(request, tournoi_id):
    # Récupération de tous les objets Tournoi enregistrés en base de données
    tournois_list = Tournoi.objects.all()
    # Récupération de l'objet Tournoi correspondant à l'ID fourni
    tournoi = Tournoi.objects.get(id=tournoi_id)
    # Récupération de toutes les poules associées au tournoi courant
    poules = Poule.objects.filter(tournoi=tournoi)
    context = {'tournoi': tournoi, 'poules': poules,
               'tournois_list': tournois_list}
    # Affichage de la page de détails du tournoi courant
    return render(request, 'tournois/tournoi.html', context)


def poule(request, poule_id):
    # Récupération de l'objet Poule correspondant à l'identifiant poule_id dans la base de données
    poule = Poule.objects.get(pk=poule_id)
    # Création du contexte de la vue, contenant la poule, les matchs de la poule et le classement des équipes dans la poule
    context = {
        'poule': poule,
        'matches': poule.get_matches(),
        'standings': poule.get_standings(),
    }
    # Affichage du template detail_poule.html avec le contexte créé précédemment
    return render(request, 'tournois/detail_poule.html', context)


def match(request, match_id):
    # Récupération de l'objet Match correspondant à l'identifiant match_id dans la base de données
    match = get_object_or_404(Match, id=match_id)
    # Création du contexte de la vue, contenant le match
    context = {'match': match}
    # Affichage du template match.html avec le contexte créé précédemment
    return render(request, 'tournois/match.html', context)
