from django.db import models

class Dados(models.Model):
    idade = models.IntegerField()
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
