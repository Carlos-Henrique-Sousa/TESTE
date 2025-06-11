from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from api.views import (
    EscolaViewSet, TurmaViewSet, ProfessorViewSet, PDTViewSet, AlunoViewSet,
    MapeamentoViewSet, PosicaoAlunoViewSet, NotasViewSet, FaltaViewSet,
    EventoEscolarViewSet, ProfessorCursoViewSet, MaterialDeEstudoViewSet, AtividadeViewSet, ResponsavelViewSet, criar_mapeamento_view,
    criar_turma, adicionar_aluno
)
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'escolas', EscolaViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'pdt', PDTViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'mapeamentos', MapeamentoViewSet)
router.register(r'posicoes-aluno', PosicaoAlunoViewSet)
router.register(r'notas', NotasViewSet)
router.register(r'faltas', FaltaViewSet)
router.register(r'eventos', EventoEscolarViewSet)
router.register(r'professor-curso', ProfessorCursoViewSet)
router.register(r'materiais', MaterialDeEstudoViewSet)
router.register(r'atividades', AtividadeViewSet, basename='atividade')
router.register(r'responsavel', ResponsavelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # fluxo com html simples
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('turma/', criar_turma, name='criar_turma'),
    path('turma/<int:turma_id>/aluno/', adicionar_aluno, name='adicionar_aluno'),
    path('mapeamento/<int:turma_id>/', criar_mapeamento_view, name='criar_mapeamento'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
