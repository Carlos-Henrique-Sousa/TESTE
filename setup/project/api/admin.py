from django.contrib import admin
from .models import (
    Escola, Turma, Professor, PDT, Aluno, Responsavel, Mapeamento,
    PosicaoAluno, Notas, Falta, EventoEscolar, ProfessorCurso,
    MaterialDeEstudo, Atividade
)

# Registra cada modelo para ficar visível no Admin
admin.site.register(Escola)
admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(PDT)
admin.site.register(Aluno)
admin.site.register(Responsavel)
admin.site.register(Mapeamento)
admin.site.register(PosicaoAluno)
admin.site.register(Notas)
admin.site.register(Falta)
admin.site.register(EventoEscolar)
admin.site.register(ProfessorCurso)
admin.site.register(MaterialDeEstudo)
admin.site.register(Atividade)
