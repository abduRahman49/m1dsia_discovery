from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, PasswordChangeForm


def index_view(request):
    return render(request, "auth/index.html")


def logout_view(request):
    logout(request)
    return redirect("login")


class UpdatePasswordView(View):

    def get(self, request):
        form = PasswordChangeForm()
        context = {"form": form}
        return render(request, "auth/change_password.html", context)
    
    def post(self, request):
        # récupérer l'utilisateur courant
        user = request.user
        print("Utilisateur connecté", user)
        # récupérer le nouveau de passe
        password = request.POST.get("password")
        user.set_password(password)
        user.save()
        return redirect("login")

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "auth/login.html", context)
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User groups", user.groups.all())
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
        role = request.POST.get("role")
        print("Rôle de l'utilisateur", role)
        #récupération du rôle
        group = Group.objects.filter(name=role).first()
        print("Group sur lequel affecter l'utilisateur", group)
        # création de l'utilisateur
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        user.groups.add(group)
        return redirect("login")
