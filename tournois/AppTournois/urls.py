from django.urls import path
from . import views
from .views import tournois

urlpatterns = [
    path('tournoi/<int:tournoi_id>/', views.tournoi, name='tournoi'),
    path('tournois/', tournois, name='tournois'),
    path('poule/<int:poule_id>/', views.detail_poule, name='detail_poule'),
    
]