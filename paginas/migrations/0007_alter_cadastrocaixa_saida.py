# Generated by Django 3.2.9 on 2021-11-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0006_auto_20211125_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrocaixa',
            name='saida',
            field=models.FloatField(),
        ),
    ]