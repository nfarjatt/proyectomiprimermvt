from django.urls import path
from familia.views import plantilla, hola_mundo


urlpatterns = [
    path("", plantilla, name="plantilla"),
    path("hola-mundo/", hola_mundo, name="hola-mundo"),
]
