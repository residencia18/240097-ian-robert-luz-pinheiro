from django.db import models

# Create your models here.
class Viagem(models.Model):
    destino = models.CharField(max_length=200)
    data_partida = models.DateTimeField(auto_now_add=False)
    durcacao = models.DurationField()
    distancia = models.BigIntegerField()
    preco = models.BigIntegerField()
    detalhes = models.TextField()

    def __str__(self):
        return self.destino