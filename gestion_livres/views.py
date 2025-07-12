from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre
from .forms import CreationLivre, UpdateLivre

# Create your views here.

def liste_livres(request):
    context = {"livres": Livre.objects.all()}
    return render(request, "gestion_livres/liste.html", context)

def detail_livre(request, id_livre):
    livre = get_object_or_404(Livre, pk=id_livre)
    context = {"livre": livre}
    return render(request, "gestion_livres/detail.html", context)

def inser_livre(request):
    if request.method == "POST":
        form = CreationLivre(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Livre.objects.create(
                titre=data.get("titre"),
                auteur=data.get("auteur"),
                annee=data.get("annee")
            )
            return redirect("liste-livres")
    else:
        form = CreationLivre()
        context = {
            "form": form
        }
        return render(request, "gestion_livres/nouveau_livre.html", context)
    
def update_livre(request, id_livre):
    livre = get_object_or_404(Livre, pk=id_livre)
    if request.method == "POST":
        form = UpdateLivre(request.POST)
        if not form.is_valid():
            print("Le formulaire n'est pas valide")
        
        data = form.cleaned_data
        if data.get("title"):
            livre.title = data.get("title")
        if data.get("auteur"):
            livre.auteur = data.get("auteur")
        if data.get("annee"):
            livre.annee = data.get("annee")
        livre.save()
        return redirect("liste-livres")
    else:
        form = UpdateLivre()
        context = {
            "form": form,
            "livre": livre
        }
        return render(request, "gestion_livres/update_livre.html", context)