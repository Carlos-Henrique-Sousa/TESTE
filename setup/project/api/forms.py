from django import forms
from .models import Turma, Aluno

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'ano', 'escola']  # adicionei 'ano' e 'escola' para ficar funcional

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'senha', 'turma', 'dificuldade_visao', 'media_humanas', 'media_exatas', 'media_linguagens']
