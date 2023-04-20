from django.urls import path
from . import views
from .views import tournois

urlpatterns = [
    # URL pour afficher la liste des tournois
    path('', tournois, name='tournois'),
    # URL pour modifier un commentaire
    path('modifier_commentaire/<int:Commentaire_id>/',
         views.modifier_commentaire, name='modifier_commentaire'),
    # URL pour commenter un match
    path('match/<int:match_id>', views.commenter, name='commenter'),
    # URL pour afficher les détails d'un tournoi
    path('tournoi/<int:tournoi_id>/', views.tournoi, name='tournoi'),
    # URL pour afficher la liste des tournois
    path('tournois/', tournois, name='tournois'),
    # URL pour afficher les détails d'une poule
    path('poule/<int:poule_id>/', views.poule, name='detail_poule'),
    # URL pour afficher les détails d'un match
    path('match/<int:match_id>/', views.match, name='match')
]
