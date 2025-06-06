from django.db import models
from django.contrib.auth.models import User

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente)
    instrucoes = models.TextField()
    equipamentos = models.TextField()
    porcoes = models.PositiveIntegerField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receitas_criadas')
    favoritos = models.ManyToManyField(User, related_name='receitas_favoritas', blank=True)

    def __str__(self):
        return self.titulo
