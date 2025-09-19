from django.db import models


class Treinador(models.Model):
    nomeT = models.CharField(max_length=35)
    idade = models.IntegerField()
    genero = models.CharField(max_length=20)
    main_pokemon = models.CharField(max_length=25)
    

    def __str__(self):
        return self.nomeT
    
def get_default_treinador():
    from app.models import Treinador
    treinador, created = Treinador.objects.get_or_create(nomeT="Nenhum", idade=10)
    return treinador.id


class Pokemon(models.Model):
    nome = models.CharField(max_length=30)
    height = models.IntegerField()
    weight = models.IntegerField()
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE, null = True, default = get_default_treinador 
    )

    def __str__(self):
        return self.nome


