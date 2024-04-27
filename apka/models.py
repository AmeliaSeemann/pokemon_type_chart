from django.db import models

# Create your models here.
class TypeChart(models.Model):
    name = models.CharField(max_length=100)
    normal = models.CharField(max_length=5)
    fire = models.CharField(max_length=5)
    water = models.CharField(max_length=5)
    electric = models.CharField(max_length=5)
    grass = models.CharField(max_length=5)
    ice = models.CharField(max_length=5)
    fighting = models.CharField(max_length=5)
    poison = models.CharField(max_length=5)
    ground = models.CharField(max_length=5)
    flying = models.CharField(max_length=5)
    psychic = models.CharField(max_length=5)
    bug = models.CharField(max_length=5)
    rock = models.CharField(max_length=5)
    ghost = models.CharField(max_length=5)
    dragon = models.CharField(max_length=5)
    dark = models.CharField(max_length=5)
    steel = models.CharField(max_length=5)
    fairy = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Colors(models.Model):
    type = models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    def __str__(self):
        return self.code