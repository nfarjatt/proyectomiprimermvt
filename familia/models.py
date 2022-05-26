from django.db import models

class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    altura = models.FloatField()
    fecha_nacimiento = models.DateField()
    email = models.TextField(default="")

    def calcular_edad(self):
        return 2022 - self.fecha_nacimiento.year
