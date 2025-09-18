from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=30)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.nome

class Treinador(models.Model):
    nome = models.CharField(max_length=35)
    idade = models.IntegerField()
    genero = models.CharField(max_length=20)
    main_pokemon = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

