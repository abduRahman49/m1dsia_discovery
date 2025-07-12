from django.urls import path
from .views import liste_livres, detail_livre, inser_livre, update_livre

urlpatterns = [
    path("liste-livres", liste_livres, name="liste-livres"),
    path("livres/<int:id_livre>", detail_livre, name="detail-livre"),
    path("livres/nouveau", inser_livre, name="inserer-livre"),
    path("livres/update/<int:id_livre>", update_livre, name="update-livre"),
]
