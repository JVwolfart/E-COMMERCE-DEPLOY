# Generated by Django 4.0.3 on 2022-04-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_livro_ativo_alter_livro_excerto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='status',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='aberto',
            field=models.BooleanField(default=True),
        ),
    ]
