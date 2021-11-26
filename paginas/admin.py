from django.contrib import admin

# Register your models here.
from .models import CadastroAluno, CadastroProfissional, CadastroTerapia

admin.site.register(CadastroAluno)
admin.site.register(CadastroProfissional)
admin.site.register(CadastroTerapia)
