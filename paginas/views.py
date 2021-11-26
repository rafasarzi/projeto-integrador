
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from paginas.models import CadastroAlunos, CadastroProfissional, CadastroTerapia
from django.urls import reverse_lazy

# Create your views here.


class InicioView(TemplateView):
    template_name = "paginas/modelo.html"


class SobreView(TemplateView):
    template_name = "paginas/sobre.html"


# # class PaginaAlunos(TemplateView):
# #     template_name = "paginas/alunos.html"


# class PaginaProfessores(TemplateView):
#     template_name = "paginas/professores.html"


# class PaginaAulas(TemplateView):
#     template_name = "paginas/aulas.html"


# class PaginaCaixa(TemplateView):
#     template_name = "paginas/caixa.html"


class CadastroCreate(CreateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroAlunos
    fields = ['nome', 'cpf', 'idade', 'email', 'telefone']
    success_url = reverse_lazy('cadastrar-aluno')


class ProfissionalCreate(CreateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroProfissional
    fields = ['nome', 'cpf', 'email', 'telefone', 'terapia']
    success_url = reverse_lazy('cadastrar-professor')


class TerapiaCreate(CreateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroTerapia
    fields = ['terapia']
    success_url = reverse_lazy('cadastrar-terapia')

########## UPDATE ##########


class CadastroUpdate(UpdateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroAlunos
    fields = ['nome', 'cpf', 'idade', 'email', 'telefone']
    success_url = reverse_lazy('cadastrar-aluno')


class ProfissionalUpdate(UpdateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroProfissional
    fields = ['nome', 'cpf', 'email', 'telefone', 'terapia']
    success_url = reverse_lazy('cadastrar-professor')


class TerapiaUpdate(UpdateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroTerapia
    fields = ['terapia']
    success_url = reverse_lazy('cadastrar-terapia')
