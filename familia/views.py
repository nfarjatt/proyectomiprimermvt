from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from familia.models import *
from django.template import loader

def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def plantilla(request):
    Personas = Persona.objects.all()
    nahuel = Persona.objects.first()
    return HttpResponse(render(request, "familia/index.html", {"about" : nahuel}))

