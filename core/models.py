from django.db import models

# Create your models here.


class Cursos(models.Model):
    idCurso = models.CharField('Id do curso', max_length=100)
    quantidadeHomens = models.CharField('Quantidade Homens', max_length=100)
    quantidadeMulheres = models.CharField('Quantidade Mulheres', max_length=100)