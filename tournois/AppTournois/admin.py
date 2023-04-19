from django.contrib import admin

from .models import Tournoi, Equipe, Match, Poule, commentaire

admin.site.register(Tournoi)
admin.site.register(Equipe)
admin.site.register(Match)
admin.site.register(Poule)
admin.site.register(commentaire)

