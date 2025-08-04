from django.shortcuts import render
# Disable CSRF checks
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from django.views import View
from django.http import HttpResponse

# Vue basée sur une fonction (gère par défaut les requetes de type GET)
def hello_view(request, pk):
    return HttpResponse(f"Hello {pk}!" if pk else "Hello world!")

# Vue basée sur une classe
@method_decorator(csrf_exempt, name="dispatch") # Ignore la protection csrf
class HiView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Handler pour méthode GET")

    def post(self, request, *args, **kwargs):
        return HttpResponse("Handler pour méthode POST")

    def put(self, request, *args, **kwargs):
        return HttpResponse("Handler pour méthode PUT")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("Handler pour méthode DELETE")


@permission_required("brique1.valider_tache")
def responsabe_dashboard_view(request):
    return render(request, "brique1/responsable.html")

@permission_required("brique1.consulter_tache")
def membre_dashboard_view(request):
    return render(request, "brique1/membre.html")
