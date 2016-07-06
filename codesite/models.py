from django.db import models

# Create your models here.

class Pessoa(models.Model):
	nome = models.CharField(max_length=254)
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.nome, self.email # Transforma o nome do campo legivel para seres humanos. maneira que vai ser vizualizado
		


class Cliente(models.Model):
	nome = models.CharField(max_length=250)

	def __str__(self):
		return self.nome



		