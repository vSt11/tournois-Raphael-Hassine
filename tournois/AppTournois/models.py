from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator
# Importation du modèle User de Django
from django.contrib.auth.models import User
# Importation de la classe Model de Django
from django.db import models

# Définition du modèle Commentaire


class Commentaire(models.Model):
    # Clé étrangère vers le modèle User de Django, pour stocker l'auteur du commentaire
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    # Clé étrangère vers le modèle Match de l'application, pour stocker le match lié au commentaire
    match = models.ForeignKey('Match', on_delete=models.CASCADE,
                              related_name='commentaire', null=True, blank=True)
    # Champ pour stocker la date et l'heure de création du commentaire, automatiquement généré par Django
    date_heure = models.DateTimeField(auto_now_add=True)
    # Champ pour stocker le contenu du commentaire (un texte)
    contenu = models.TextField()

    # Afficher la chaine de caractère et non l'objet
    def __str__(self):
        return self.contenu


class Equipe(models.Model):
    # Champ de nom d'équipe avec une longueur maximale de 255 caractères
    nom_equipe = models.CharField(max_length=255)
    # Champ de nom d'entraîneur avec une longueur maximale de 255 caractères
    nom_entraineur = models.CharField(max_length=255)
    # Champ de joueurs sous forme de texte
    joueurs = models.TextField()

    # Méthode qui récupère les matchs joués par l'équipe
    def get_matchs_joues(self):
        # Récupération des matchs où l'équipe est l'équipe 1
        matchs_equipe1 = Match.objects.filter(equipe1=self)
        # Récupération des matchs où l'équipe est l'équipe 2
        matchs_equipe2 = Match.objects.filter(equipe2=self)
        # Concaténation des deux listes de matchs et élimination des doublons
        return (matchs_equipe1 | matchs_equipe2).distinct()

    # Méthode qui retourne une chaîne représentant l'objet
    def __str__(self):
        return self.nom_equipe


class Poule(models.Model):
    numero_poule = models.IntegerField()
    tournoi = models.ForeignKey('Tournoi', on_delete=models.CASCADE)
    equipes = models.ManyToManyField('Equipe')

    def __str__(self):
        return f"Poule {self.numero_poule} - Tournoi {self.tournoi}"

    def get_matches(self):
        # Retourne tous les matches de la poule
        return Match.objects.filter(numero_poule=self)

    def get_teams(self):
        # Retourne toutes les équipes de la poule
        return self.equipes.all()

    def get_team_count(self):
        # Retourne le nombre d'équipes associées à la poule
        return self.equipes.count()

    def get_standings(self):
        # Récupère la liste des équipes de la poule
        teams = self.get_teams()
        # Initialise la variable de classement
        standings = []

        # Pour chaque équipe de la poule, calcule son nombre de points, de buts marqués, de buts encaissés, etc.
        for team in teams:
            points = 0
            goals_for = 0
            goals_against = 0

            # Récupère les matches joués par l'équipe courante
            matches = self.get_matches().filter(Q(equipe1=team) | Q(equipe2=team))

            # Parcourt chaque match pour calculer les statistiques de l'équipe
            for match in matches:
                if match.equipe1 == team:
                    # L'équipe courante est l'équipe à domicile dans ce match
                    goals_for += match.score_equipe1
                    goals_against += match.score_equipe2
                    if match.score_equipe1 > match.score_equipe2:
                        points += 3
                    elif match.score_equipe1 == match.score_equipe2:
                        points += 1
                else:
                    # L'équipe courante est l'équipe à l'extérieur dans ce match
                    goals_for += match.score_equipe2
                    goals_against += match.score_equipe1
                    if match.score_equipe2 > match.score_equipe1:
                        points += 3
                    elif match.score_equipe2 == match.score_equipe1:
                        points += 1

            # Ajoute les statistiques de l'équipe courante à la variable de classement
            standings.append({
                'team': team,
                'points': points,
                'goals_for': goals_for,
                'goals_against': goals_against,
                'goal_difference': goals_for - goals_against
            })

            # Trie la variable de classement selon les règles habituelles
            standings = sorted(
                standings, key=lambda k: (-k['points'], -k['goal_difference'], -k['goals_for']))

            # Retourne le classement
        return standings


class Tournoi(models.Model):
    nom_tournoi = models.CharField(max_length=255)  # Nom du tournoi
    liste_equipes = models.ManyToManyField(
        'Equipe')  # Liste des équipes participantes
    nb_poules = models.IntegerField()  # Nombre de poules dans le tournoi
    nb_equipes_poule = models.IntegerField()  # Nombre d'équipes dans chaque poule
    # Lieu du tournoi (optionnel)
    lieu = models.CharField(max_length=255, null=True, blank=True)
    # Dates du tournoi (optionnel)
    dates = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # Retourne le nom du tournoi lorsqu'on le convertit en chaîne de caractères
        return self.nom_tournoi


class Match(models.Model):
    # Date et heure du match
    date_heure = models.DateTimeField()
    # Lieu où se déroule le match
    lieu = models.CharField(max_length=255)
    # Équipe 1 du match
    equipe1 = models.ForeignKey(
        'Equipe', related_name='equipe1', on_delete=models.CASCADE)
    # Équipe 2 du match
    equipe2 = models.ForeignKey(
        'Equipe', related_name='equipe2', on_delete=models.CASCADE)
    # Score de l'équipe 1
    score_equipe1 = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    # Score de l'équipe 2
    score_equipe2 = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    # Numéro de la poule à laquelle appartient le match
    numero_poule = models.ForeignKey(
        'Poule', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        # Format de la chaîne de caractères retournée
        return f"Match {self.id} : {self.equipe1} vs {self.equipe2} ({self.date_heure} - {self.lieu})"
