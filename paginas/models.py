from django.db import models


class CadastroAlunos(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.DecimalField(decimal_places=1, max_digits=11)
    idade = models.CharField(max_length=50)
    email = models.EmailField(max_length=155)
    telefone = models.FloatField(max_length=10)

    def __str__(self):
        return "{} ({})" .format(self.nome, self.cpf, self.idade, self.email, self.telefone)
