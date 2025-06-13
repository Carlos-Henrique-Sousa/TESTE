from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import (
    Escola, Turma, Professor, PDT, Aluno, Mapeamento, PosicaoAluno,
    Notas, Falta, EventoEscolar, ProfessorCurso, MaterialDeEstudo, Atividade, Responsavel
)
from .serializers import (
    EscolaSerializer, TurmaSerializer, ProfessorSerializer, PDTSerializer,
    AlunoSerializer, MapeamentoSerializer, PosicaoAlunoSerializer, NotasSerializer,
    FaltaSerializer, EventoEscolarSerializer, ProfessorCursoSerializer,
    MaterialDeEstudoSerializer, AtividadeSerializer, ResponsavelSerializer
)

class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer

class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class PDTViewSet(viewsets.ModelViewSet):
    queryset = PDT.objects.all()
    serializer_class = PDTSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class MapeamentoViewSet(viewsets.ModelViewSet):
    queryset = Mapeamento.objects.all()
    serializer_class = MapeamentoSerializer

class PosicaoAlunoViewSet(viewsets.ModelViewSet):
    queryset = PosicaoAluno.objects.all()
    serializer_class = PosicaoAlunoSerializer

class NotasViewSet(viewsets.ModelViewSet):
    queryset = Notas.objects.all()
    serializer_class = NotasSerializer

class FaltaViewSet(viewsets.ModelViewSet):
    queryset = Falta.objects.all()
    serializer_class = FaltaSerializer

class EventoEscolarViewSet(viewsets.ModelViewSet):
    queryset = EventoEscolar.objects.all()
    serializer_class = EventoEscolarSerializer

class ProfessorCursoViewSet(viewsets.ModelViewSet):
    queryset = ProfessorCurso.objects.all()
    serializer_class = ProfessorCursoSerializer

class MaterialDeEstudoViewSet(viewsets.ModelViewSet):
    queryset = MaterialDeEstudo.objects.all()
    serializer_class = MaterialDeEstudoSerializer

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer

from django.shortcuts import render, get_object_or_404
from .models import Turma, Aluno, Mapeamento, PosicaoAluno

def criar_mapeamento_view(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)

    # Apaga mapeamento antigo, se existir
    Mapeamento.objects.filter(turma=turma).delete()

    # Configuração fixa só pra teste
    filas = 3
    colunas = 4
    tipo_agrupamento = "sozinho"

    mapeamento = Mapeamento.objects.create(
        turma=turma,
        filas=filas,
        colunas=colunas,
        tipo_agrupamento=tipo_agrupamento,
    )

    alunos = Aluno.objects.filter(turma=turma).order_by('nome')

    fila_atual = 1
    coluna_atual = 1

    for aluno in alunos:
        if fila_atual > filas:
            break

        PosicaoAluno.objects.create(
            mapeamento=mapeamento,
            aluno=aluno,
            fila=fila_atual,
            coluna=coluna_atual,
        )

        coluna_atual += 1
        if coluna_atual > colunas:
            coluna_atual = 1
            fila_atual += 1

    posicoes = PosicaoAluno.objects.filter(mapeamento=mapeamento).order_by('fila', 'coluna')

    context = {
        'turma': turma,
        'mapeamento': mapeamento,
        'posicoes': posicoes,
        'filas_range': range(1, filas + 1),
        'colunas_range': range(1, colunas + 1),
    }

    return render(request, 'index.html', context)

# views.py

from django.shortcuts import render, redirect
from .forms import TurmaForm, AlunoForm
from .models import Turma, Aluno

def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            turma = form.save()
            return redirect('adicionar_aluno', turma_id=turma.id)
    else:
        form = TurmaForm()
    return render(request, 'criar_turma.html', {'form': form})

def adicionar_aluno(request, turma_id):
    turma = Turma.objects.get(id=turma_id)
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adicionar_aluno', turma_id=turma.id)
    else:
        form = AlunoForm(initial={'turma': turma})
    alunos = turma.alunos.all()
    return render(request, 'adicionar_aluno.html', {'form': form, 'turma': turma, 'alunos': alunos})
