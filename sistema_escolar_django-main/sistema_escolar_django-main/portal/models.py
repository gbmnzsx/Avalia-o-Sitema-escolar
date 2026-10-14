from django.db import models

#ERRO: A falta do import do timezone estava causando um erro de importação. 
#CORREÇÃO: Importei timezone do django.utils para corrigir o erro de importação do timezone.
from django.utils import timezone


class Professor(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)
    registro = models.CharField(max_length=10)
    disciplina = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)
    observacao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)
    especialidade = models.CharField(max_length=30, blank=True)
    #ERRO: A falta do campo especialidade estava causando um erro no codigo, pois o campo especialidade era referenciado no admin.py.
    #CORREÇÃO: Adicionei o campo especialidade na classe Professor para corrigir

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    matricula = models.IntegerField(unique=True)
    criacao_data = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Aula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    horario = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)
    status = models.CharField(
        default='A',
        max_length=1,
        choices=(
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada')
        )
    )

    def __str__(self):
        return f'Aula {self.status} com sucesso.'
