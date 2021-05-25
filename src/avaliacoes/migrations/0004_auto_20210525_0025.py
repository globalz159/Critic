# Generated by Django 3.1.7 on 2021-05-25 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0003_auto_20210524_1859'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avaliacoes', '0003_auto_20210524_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacaofilme',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='avaliacaolivro',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='avaliacaoserie',
            name='data_criacao',
        ),
        migrations.AlterField(
            model_name='avaliacaofilme',
            name='item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='itens.filme'),
        ),
        migrations.AlterField(
            model_name='avaliacaofilme',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_id'),
        ),
        migrations.AlterField(
            model_name='avaliacaolivro',
            name='item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='itens.livro'),
        ),
        migrations.AlterField(
            model_name='avaliacaolivro',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_id'),
        ),
        migrations.AlterField(
            model_name='avaliacaoserie',
            name='item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='itens.serie'),
        ),
        migrations.AlterField(
            model_name='avaliacaoserie',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_id'),
        ),
    ]
