from django.urls import path
from .views import bonjour_view, book_count_view, book_detail

urlpatterns = [
    path("bonjour/<str:username>/", bonjour_view),
    path("livres/liste/", book_count_view),
    path("livre/<int:book_id>/", book_detail),
]