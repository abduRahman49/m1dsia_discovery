from django import forms


class CreationLivre(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100)
    auteur = forms.CharField(label="Auteur", max_length=100)
    annee = forms.IntegerField(label="Annee")


class UpdateLivre(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100, required=False)
    auteur = forms.CharField(label="Auteur", max_length=100, required=False)
    annee = forms.IntegerField(label="Annee", required=False)
