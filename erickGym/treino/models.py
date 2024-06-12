from django.db import models
from cadastro.models import Aluno, Professor

# Create your models here.

class Exercicio(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=250, blank=False, null=False)
    ativo = models.BooleanField(default=True, blank=False, null=False)
    
    
class Treino(models.Model):
    aluno = models.ForeignKey(Aluno, verbose_name='treino', on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, related_name='treino', on_delete=models.CASCADE)
    
    
class ItemTreino(models.Model):
    exercicio = models.ForeignKey(Exercicio, verbose_name='item_treino', on_delete=models.CASCADE)
    series = models.IntegerField(blank=False, null=False)
    repeticoes = models.IntegerField(blank=False, null=False)
    peso = models.IntegerField()
    treino = models.ForeignKey(Treino, verbose_name='item_treino', on_delete=models.CASCADE)
    
    