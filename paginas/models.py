from django.db import models


class CadastroAluno(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    idade = models.CharField(max_length=50)
    email = models.EmailField(max_length=155)
    telefone = models.IntegerField()

    def __str__(self):
        return "{} ({})" .format(self.nome, self.cpf, self.idade, self.email, self.telefone)


class CadastroProfissional(models.Model):
    nome = models.CharField(max_length=155)
    cpf = models.IntegerField()
    email = models.EmailField(max_length=155)
    telefone = models.IntegerField()
    terapia = models.CharField(max_length=155)

    def __str__(self):
        return "{} ({})" .format(self.nome, self.cpf, self.email, self.telefone, self.terapia)


class CadastroEntrada(models.Model):
    valor = models.IntegerField()
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return "{} ({})" .format(self.valor, self.descricao)


class CadastroSaida(models.Model):
    valor = models.IntegerField()
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return "{} ({})" .format(self.valor, self.descricao)
