from familia.views import *
from django.urls import path


urlpatterns = [
    path("hola-mundo/", hola_mundo, name="hola-mundo"),
    path("plantilla/", plantilla, name="plantilla"),
]