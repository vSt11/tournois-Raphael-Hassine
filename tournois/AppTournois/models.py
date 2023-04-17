from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator

class Equipe(models.Model):
    nom_equipe = models.CharField(max_length=255)
    nom_entraineur = models.CharField(max_length=255)
    joueurs = models.TextField()
    
    def get_matchs_joues(self):
        matchs_equipe1 = Match.objects.filter(equipe1=self)
        matchs_equipe2 = Match.objects.filter(equipe2=self)
        return (matchs_equipe1 | matchs_equipe2).distinct()
    
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

    def get_standings(self):
        # Calcule le classement de la poule
        teams = self.get_teams()
        standings = []
        for team in teams:
            points = 0
            goals_for = 0
            goals_against = 0
            matches = self.get_matches().filter(Q(equipe1=team) | Q(equipe2=team))
            for match in matches:
                if match.equipe1 == team:
                    goals_for += match.score_equipe1
                    goals_against += match.score_equipe2
                    if match.score_equipe1 > match.score_equipe2:
                        points += 3
                    elif match.score_equipe1 == match.score_equipe2:
                        points += 1
                else:
                    goals_for += match.score_equipe2
                    goals_against += match.score_equipe1
                    if match.score_equipe2 > match.score_equipe1:
                        points += 3
                    elif match.score_equipe2 == match.score_equipe1:
                        points += 1
            standings.append({
                'team': team,
                'points': points,
                'goals_for': goals_for,
                'goals_against': goals_against,
                'goal_difference': goals_for - goals_against
            })
        standings = sorted(standings, key=lambda k: (-k['points'], -k['goal_difference'], -k['goals_for']))
        return standings
    
class Tournoi(models.Model):
    nom_tournoi = models.CharField(max_length=255)
    liste_equipes = models.ManyToManyField('Equipe')
    nb_poules = models.IntegerField()
    nb_equipes_poule = models.IntegerField()
    lieu = models.CharField(max_length=255, null=True, blank=True)
    dates = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.nom_tournoi


class Match(models.Model):
    date_heure = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    #equipe1 = models.ForeignKey('Equipe', on_delete=models.CASCADE, related_name='matchs_joues1')
    #equipe2 = models.ForeignKey('Equipe', on_delete=models.CASCADE, related_name='matchs_joues2')
    equipe1 = models.ForeignKey('Equipe', related_name='equipe1', on_delete=models.CASCADE)
    equipe2 = models.ForeignKey('Equipe', related_name='equipe2', on_delete=models.CASCADE)
    score_equipe1 = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    score_equipe2 = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    numero_poule = models.ForeignKey('Poule', on_delete=models.CASCADE, null=True, blank=True)        

    def __str__(self):
        return f"Match {self.id} : {self.equipe1} vs {self.equipe2} ({self.date_heure} - {self.lieu})"
