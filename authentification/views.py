from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm


def index_view(request):
    return render(request, "auth/index.html")


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "auth/login.html", context)
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")

        messages.add_message(request, messages.INFO, "Vos identifiants sont invalides")
        return redirect("login")


class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        context = {"form": form}
        return render(request, "auth/registration.html", context)
    
    def post(self, request):
        # extraction des informations soumises depuis le formulaire
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # création de l'utilisateur
        User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        return redirect("login")
