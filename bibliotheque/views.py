from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
# Ignorer les tokens csrf
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Book

def hello(request):
    # render prend au minimum deux arguments (request, le template)
    # En plus on peut avoir le context (données fournies au template)
    context = {"nom": "seye", "prenom": "abdou"}
    return render(request, 'bibliotheque/index.html', context)

@csrf_exempt
def bonjour_view(request, username):
    return HttpResponse(f"Bonjour {username}" if username else "Bonjour Anonyme")

def book_count_view(request):
    nombre_livres = Book.objects.count()
    message = f"Il y a actuellement {nombre_livres} livres enregistrés."
    return HttpResponse(message)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    description = f"""
        Titre: {book.title}\n
        Auteur: {book.author}\n
        Annee: {book.published_year}\n
    """
    return HttpResponse(description)


class WelcomeView(View):

    def get(self, request, username, *args, **kwargs):
        message = f"Bienvenue, {username} !"
        return HttpResponse(message)


class BooksBeforeView(View):
    def get(self, request, year, *args, **kwargs):
        books_before = Book.objects.filter(published_year__lt=year)
        liste_livres = ", ".join(book.title for book in books_before)
        return HttpResponse(liste_livres)

@method_decorator(csrf_exempt, name="dispatch")
class BookView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Utilisez POST pour ajouter un livre.")
    
    def post(self, request, *args, **kwargs):
        print("Les données soumises par formulaire", request.POST)
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_year = request.POST.get("published_year")
        book = Book.objects.create(title=title, author=author, published_year=published_year)
        message = f"Vous avez créé avec succès le livre {book.title} : ID {book.id}"
        return HttpResponse(message)
