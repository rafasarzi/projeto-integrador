# Generated by Django 3.2.9 on 2021-11-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_rename_inscricao_cadastro'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.DecimalField(decimal_places=1, max_digits=11)),
                ('idade', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=155)),
                ('telefone', models.FloatField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Cadastro',
        ),
    ]