
from django.views.generic.edit import CreateView
from paginas.models import CadastroAlunos
from django.urls import reverse_lazy

# Create your views here.


# # class HomeView(TemplateView):
# #     template_name = "paginas/home.html"


# class CadastroCreate(TemplateView):
#     template_name = "paginas/cadastro.html"


# class IndexView(TemplateView):
#     template_name = "paginas/index.html"


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
    fields = ['name', 'cpf', 'idade', 'email', 'telefone', ]
    success_url = reverse_lazy('home')
