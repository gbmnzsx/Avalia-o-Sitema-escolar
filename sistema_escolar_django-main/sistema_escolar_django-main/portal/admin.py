from django.contrib import admin
from portal import models

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo',)

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'professor', 'status',)


#ERRO:Nao é necessario cirar aluno id e professor id, pois o django ja cria automaticamente um id para cada objeto criado.
#CORREÇÃO: Removi os campos aluno_id e professor_id da classe AulaAdmin, pois o django ja cria automaticamente um id para cada objeto criado.