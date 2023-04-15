from django.db import models

class Equipe(models.Model):
    nom_equipe = models.CharField(max_length=255)
    nom_entraineur = models.CharField(max_length=255)
    joueurs = models.TextField()

class Poule(models.Model):
    numero_poule = models.IntegerField()
    tournoi = models.ForeignKey('Tournoi', on_delete=models.CASCADE)
    equipes = models.ManyToManyField('Equipe')

class Tournoi(models.Model):
    nom_tournoi = models.CharField(max_length=255)
    liste_equipes = models.ManyToManyField('Equipe')
    nb_poules = models.IntegerField()
    nb_equipes_poule = models.IntegerField()
    lieu = models.CharField(max_length=255, null=True, blank=True)
    dates = models.DateTimeField(null=True, blank=True)

class Match(models.Model):
    date_heure = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    equipe1 = models.ForeignKey('Equipe', on_delete=models.CASCADE, related_name='matchs_joues1')
    equipe2 = models.ForeignKey('Equipe', on_delete=models.CASCADE, related_name='matchs_joues2')
    score = models.CharField(max_length=255, null=True, blank=True)
    numero_poule = models.ForeignKey('Poule', on_delete=models.CASCADE, null=True, blank=True)