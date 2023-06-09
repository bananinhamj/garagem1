# Generated by Django 4.1.7 on 2023-03-31 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0006_cor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(blank=True, default=0, null=True)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categoria', to='garagem.categoria')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cor', to='garagem.cor')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculo', to='garagem.marca')),
            ],
        ),
    ]
