from django.db import models
from django.contrib.auth.models import User
# from treino.models import 

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=300, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    idade = models.IntegerField(blank=False, null=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno', null=True, blank=False)
    

class Professor(models.Model):
    nome = models.CharField(max_length=300, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor', null=True, blank=False)