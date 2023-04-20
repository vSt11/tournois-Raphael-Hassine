# Ce code définit un formulaire pour le modèle Commentaire.
# Il importe la classe forms depuis le module django et le modèle Commentaire depuis le fichier models.py de l'application.
# La classe CommentaireForm hérite de forms.ModelForm, ce qui permet de générer un formulaire à partir du modèle Commentaire.
# La classe Meta spécifie le modèle à utiliser (Commentaire) et les champs du formulaire à inclure (contenu).
from django import forms
from .models import Commentaire


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
