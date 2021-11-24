from django.urls import path
from django.urls import path
from .views import CadastroCreate, SobreView, InicioView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', InicioView.as_view(), name='index'),

    path('sobre/', SobreView.as_view(), name='sobre'),

    path('paginas/cadastro/', CadastroCreate.as_view(), name='cadastrar-aluno'),



    # # path('', CreateView.as_view(), name='home'),
    # path('cadastro/', .as_view(), name='cadastro'),
    # # path('inicio/', IndexView.as_view(), name='inicio'),
    # # path('alunos/', PaginaAlunos.as_view(), name='alunos'),
    # # path('professores/', PaginaProfessores.as_view(), name='professores'),
    # # path('aulas/', PaginaAulas.as_view(), name='aulas'),
    # # path('caixa/', PaginaCaixa.as_view(), name='caixa'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
