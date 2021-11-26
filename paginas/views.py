
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from paginas.models import CadastroAluno, CadastroProfissional, CadastroTerapia
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

########## CRIAR ##########
class CadastroCreate(CreateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroAluno
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
    model = CadastroAluno
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

########## DELETE ##########


class CadastroDelete(DeleteView):
    template_name = 'paginas/cadastro-excluir.html'
    model = CadastroAluno
    success_url = reverse_lazy('cadastrar-aluno')


class ProfissionalDelete(DeleteView):
    template_name = 'paginas/cadastro-excluir.html'
    model = CadastroProfissional
    success_url = reverse_lazy('cadastrar-professor')


class TerapiaDelete(DeleteView):
    template_name = 'paginas/cadastro-excluir.html'
    model = CadastroTerapia
    success_url = reverse_lazy('cadastrar-terapia')

########## LISTA ##########


class CadastroList(ListView):
    template_name = 'paginas/listar/alunos.html'
    model = CadastroAluno


class ProfissionalList(ListView):
    template_name = 'paginas/listar/profissionais.html'
    model = CadastroProfissional


class TerapiaList(ListView):
    template_name = 'paginas/listar/terapias.html'
    model = CadastroTerapia
