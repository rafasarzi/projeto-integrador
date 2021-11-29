
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
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
    success_url = reverse_lazy('listar-aluno')


class ProfissionalCreate(CreateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroProfissional
    fields = ['nome', 'cpf', 'email', 'telefone', 'terapia']
    success_url = reverse_lazy('listar-profissional')


class TerapiaCreate(CreateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroTerapia
    fields = ['terapia', 'descrição']
    success_url = reverse_lazy('listar-terapia')

########## UPDATE ##########


class CadastroUpdate(UpdateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroAlunos
    fields = ['nome', 'cpf', 'idade', 'email', 'telefone']
    success_url = reverse_lazy('listar-aluno')


class ProfissionalUpdate(UpdateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroProfissional
    fields = ['nome', 'cpf', 'email', 'telefone', 'terapia']
    success_url = reverse_lazy('listar-profissional')


class TerapiaUpdate(UpdateView):
    template_name = 'paginas/cadastro.html'
    model = CadastroTerapia
    fields = ['terapia', 'descrição']
    success_url = reverse_lazy('listar-terapia')

########## DELETE ##########


class CadastroDelete(DeleteView):
    template_name = 'paginas/cadastro-excluir.html'
    model = CadastroAlunos
    success_url = reverse_lazy('listar-aluno')


class ProfissionalDelete(DeleteView):
    template_name = 'paginas/cadastro-excluir.html'
    model = CadastroProfissional
    success_url = reverse_lazy('listar-profissional')


class TerapiaDelete(DeleteView):
    template_name = 'paginas/cadastro-excluir.html'
    model = CadastroTerapia
    success_url = reverse_lazy('listar-terapia')

########## LISTAR ##########


class CadastroList(ListView):
    template_name = 'paginas/listas/alunos.html'
    model = CadastroAlunos


class ProfissionalList(ListView):
    template_name = 'paginas/listas/professores.html'
    model = CadastroProfissional


class TerapiaList(ListView):
    template_name = 'paginas/listas/aulas.html'
    model = CadastroTerapia
