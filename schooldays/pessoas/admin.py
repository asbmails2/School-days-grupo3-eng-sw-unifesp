from django.contrib import admin

# Register your models here.
from .models import Aluno, Responsavel, Professor, Colaborador



admin.site.register(Aluno)
admin.site.register(Responsavel)
admin.site.register(Professor)
admin.site.register(Colaborador)
