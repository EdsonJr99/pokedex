from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=30)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.nome
