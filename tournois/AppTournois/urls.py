from django.urls import path
from . import views
from .views import tournois

urlpatterns = [
    path('', tournois, name='tournois'),
    path('tournoi/<int:tournoi_id>/', views.tournoi, name='tournoi'),
    path('tournois/', tournois, name='tournois'),
    path('poule/<int:poule_id>/', views.poule, name='detail_poule'),    
    path('match/<int:match_id>/', views.match, name='match')]