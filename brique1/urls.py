from django.urls import path
from .views import hello_view, HiView

urlpatterns = [
    path('hello/<int:pk>/', hello_view),
    path('hi/', HiView.as_view())
]
