from django.contrib import admin

# Register your models here.
from .models import CadastroAluno, CadastroProfissional, CadastroEntrada, CadastroSaida

admin.site.register(CadastroAluno)
admin.site.register(CadastroProfissional)
admin.site.register(CadastroEntrada)
admin.site.register(CadastroSaida)
