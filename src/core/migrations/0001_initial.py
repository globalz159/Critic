# Generated by Django 3.1.7 on 2021-04-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('username', models.CharField(max_length=30, verbose_name='Nome de Usuário')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('senha', models.CharField(max_length=100, verbose_name='Senha')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
            ],
        ),
    ]
