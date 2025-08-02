from django import forms
from django.contrib.auth.models import Group


class RegistrationForm(forms.Form):
    # Choices doit être une liste de tuples
    CHOICES = [
        (role.name, role.name)
        for role in Group.objects.all() # le tuple est créé à partir de l'attribut name de l'instance Group
    ]

    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    email = forms.EmailField(label="Adresse email")
    role = forms.ChoiceField(label="Rôle", choices=CHOICES)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput())


class PasswordChangeForm(forms.Form):
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput())
