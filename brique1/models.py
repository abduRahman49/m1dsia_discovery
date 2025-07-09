from django.db import models
from django.conf import settings


class Categorie(models.Model):
    libelle = models.CharField(max_length=100)
    # tache_set


class ListeTache(models.Model):
    libelle = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
    # taches


class Tache(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField()
    est_terminee = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(null=True)
    listes_taches = models.ManyToManyField(ListeTache, related_name="taches")
    categorie = models.ForeignKey(Categorie, null=True,
                                  on_delete=models.SET_NULL)
    # categorie_id


class Profil(models.Model):
    STANDARD = "standard"
    VERIFICATEUR = "verificateur"
    ADMIN = "admin"

    PROFIL = (
        (STANDARD, 'Standard'),
        (VERIFICATEUR, 'Verificateur'),
        (ADMIN, 'Admin')
    )

    libelle = models.CharField(choices=PROFIL, default=STANDARD)
    utilisateur = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
