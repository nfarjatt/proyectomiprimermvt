from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from familia.models import Persona


def hola_mundo(request):
    return HttpResponse("Hola Mundo")


def plantilla(request):
    consulta = Persona.objects.all()
    return HttpResponse(render(request, "familia/index.html", {"personas": consulta}))
