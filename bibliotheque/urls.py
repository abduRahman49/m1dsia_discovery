from django.urls import path
from .views import (
    hello,
    bonjour_view,
    book_count_view,
    book_detail,
    WelcomeView,
    BooksBeforeView,
    BookView
)


urlpatterns = [
    path("bonjour/<str:username>/", bonjour_view),
    path("livres/liste/", book_count_view),
    path("livre/<int:book_id>/", book_detail),
    path("welcome/<str:username>/", WelcomeView.as_view()),
    path("books/before/<int:year>/", BooksBeforeView.as_view()),
    path("books/new/", BookView.as_view()),
    path("hello/", hello),
]
