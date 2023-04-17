from django import forms
from .models import commentaire

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = commentaire
        fields = ['auteur', 'match', 'contenu']
        
