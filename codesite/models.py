from django.db import models


# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mensagem = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
        # Transforma o nome do campo legivel para seres humanos. maneira que vai ser vizualizado


class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome
