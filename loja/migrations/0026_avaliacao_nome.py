# Generated by Django 4.0.3 on 2022-04-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0025_alter_avaliacao_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='nome',
            field=models.CharField(default='Anônimo', max_length=255),
        ),
    ]
