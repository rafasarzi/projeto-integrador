from django.urls import path
from django.urls import path


from .views import CadastroCreate, SobreView, InicioView, ProfissionalCreate, TerapiaCreate
from .views import CadastroUpdate, ProfissionalUpdate, TerapiaUpdate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', InicioView.as_view(), name='index'),

    path('sobre/', SobreView.as_view(), name='sobre'),

    path('aluno/', CadastroCreate.as_view(),
         name='cadastrar-aluno'),

    path('profissional/', ProfissionalCreate.as_view(),
         name='cadastrar-professor'),

    path('terapia/', TerapiaCreate.as_view(),
         name='cadastrar-terapia'),

    path('editar/aluno/<int:pk>', CadastroUpdate.as_view(),
         name='editar-aluno'),

    path('editar/profissional/<int:pk>', ProfissionalUpdate.as_view(),
         name='editar-profissional'),

    path('editar/terapia/<int:pk>', TerapiaUpdate.as_view(),
         name='editar-terapia'),



    # # path('', CreateView.as_view(), name='home'),
    # path('cadastro/', .as_view(), name='cadastro'),
    # # path('inicio/', IndexView.as_view(), name='inicio'),
    # # path('alunos/', PaginaAlunos.as_view(), name='alunos'),
    # # path('professores/', PaginaProfessores.as_view(), name='professores'),
    # # path('aulas/', PaginaAulas.as_view(), name='aulas'),
    # # path('caixa/', PaginaCaixa.as_view(), name='caixa'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
