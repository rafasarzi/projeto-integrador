from django.urls import path
from django.urls import path


from .views import CadastroCreate, SobreView, InicioView, ProfissionalCreate
from .views import CadastroUpdate, ProfissionalUpdate
from .views import CadastroDelete, ProfissionalDelete
from .views import CadastroList, ProfissionalList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', InicioView.as_view(), name='index'),

    path('sobre/', SobreView.as_view(), name='sobre'),

    path('aluno/', CadastroCreate.as_view(),
         name='cadastrar-aluno'),

    path('profissional/', ProfissionalCreate.as_view(),
         name='cadastrar-profissional'),


    path('editar/aluno/<int:pk>/', CadastroUpdate.as_view(),
         name='editar-aluno'),

    path('editar/profissional/<int:pk>/', ProfissionalUpdate.as_view(),
         name='editar-profissional'),


    path('excluir/aluno/<int:pk>', CadastroDelete.as_view(),
         name='excluir-aluno'),

    path('excluir/profissional/<int:pk>', ProfissionalDelete.as_view(),
         name='excluir-profissional'),



    path('listar/aluno', CadastroList.as_view(),
         name='listar-aluno'),

    path('listar/profissional', ProfissionalList.as_view(),
         name='listar-profissional'),




    # # path('', CreateView.as_view(), name='home'),
    # path('cadastro/', .as_view(), name='cadastro'),
    # # path('inicio/', IndexView.as_view(), name='inicio'),
    # # path('alunos/', PaginaAlunos.as_view(), name='alunos'),
    # # path('professores/', PaginaProfessores.as_view(), name='professores'),
    # # path('aulas/', PaginaAulas.as_view(), name='aulas'),
    # # path('caixa/', PaginaCaixa.as_view(), name='caixa'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
