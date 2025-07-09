from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book


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