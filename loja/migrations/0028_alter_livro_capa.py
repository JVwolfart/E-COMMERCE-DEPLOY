# Generated by Django 4.0.4 on 2022-05-19 12:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0027_alter_avaliacao_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
