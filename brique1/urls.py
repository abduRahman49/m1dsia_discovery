from django.urls import path
from .views import hello_view, HiView, responsabe_dashboard_view, membre_dashboard_view

urlpatterns = [
    path('hello/<int:pk>/', hello_view),
    path('hi/', HiView.as_view()),
    path('dashboard-resp/', responsabe_dashboard_view),
    path('dashboard-membre/', membre_dashboard_view),
    path('hi/', HiView.as_view()),
]
