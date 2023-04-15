from django.contrib import admin

from .models import Tournoi, Equipe, Match

admin.site.register(Tournoi)
admin.site.register(Equipe)
admin.site.register(Match)
