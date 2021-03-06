# Generated by Django 4.0.3 on 2022-04-28 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0020_statuspedido_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant', models.IntegerField(blank=True, null=True)),
                ('valor_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('total_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loja.livro')),
            ],
        ),
    ]
