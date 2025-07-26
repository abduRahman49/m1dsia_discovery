from django.urls import path
from .views import RegistrationView, LoginView, index_view

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("home/", index_view, name="index"),
]