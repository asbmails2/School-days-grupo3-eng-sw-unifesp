from typing import Any
from django.db import models
from pessoas.models import Professor,Aluno

class Disciplina(models.Model):
    # Basic Discipline Information
    nome = models.CharField(max_length=255, verbose_name='Nome da Disciplina')
    codigo = models.CharField(max_length=10, unique=True, verbose_name='Código da Disciplina')
    carga_horaria = models.IntegerField(verbose_name='Horas Aula')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='turma', verbose_name='Professor')
    faltasMAx = 10
    diaDaSemana = [] #aulas da disciplina por professor
    horarioAula = [] #hora início e fim de acordo com  odia da seman referente

    def __str__(self):
        return self.nome
    
    
class Turma(models.Model):
    nome = models.CharField(max_length=20, verbose_name='nome da turma')
    #ano que a turma foi realizada - fica a relação de alunos, disciplinas e notas 
    ano_ocorrencia = models.IntegerField(verbose_name='Ano de Ocorrência')
    #antiga série
    ano = models.IntegerField(verbose_name='Ano')

    # Many-to-many relationship with Aluno (Student)
    alunos = models.ForeignKey(Aluno,on_delete=models.CASCADE)

    # Many-to-many relationship with Disciplina (Discipline)
    disciplinas = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

class Notas (models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = 0.0
    faltas = 0



    