from django.contrib import admin

# Register your models here.
from .models import CadastroAlunos, CadastroProfissional, CadastroTerapia

admin.site.register(CadastroAlunos)
admin.site.register(CadastroProfissional)
admin.site.register(CadastroTerapia)
