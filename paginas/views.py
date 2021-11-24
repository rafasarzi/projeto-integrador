
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from paginas.models import CadastroAlunos
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
    fields = ['nome', 'cpf', 'idade', 'email', 'telefone', ]
    success_url = reverse_lazy('home')
