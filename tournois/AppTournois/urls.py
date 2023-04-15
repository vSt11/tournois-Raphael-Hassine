from django.urls import path
from . import views
from .views import tournois

urlpatterns = [
    path("", views.index, name="index"),
    path('tournois/', tournois, name='tournois')
    
]