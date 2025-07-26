from django.urls import path
from .views import RegistrationView, LoginView, index_view, logout_view, UpdatePasswordView

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("home/", index_view, name="index"),
    path("change-password/", UpdatePasswordView.as_view(), name="update-password"),
]