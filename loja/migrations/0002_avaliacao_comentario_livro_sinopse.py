# Generated by Django 4.0.3 on 2022-04-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='sinopse',
            field=models.TextField(blank=True, null=True),
        ),
    ]
