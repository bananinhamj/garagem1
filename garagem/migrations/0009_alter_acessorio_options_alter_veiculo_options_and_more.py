# Generated by Django 4.1.7 on 2023-03-31 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0008_alter_veiculo_marca'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acessorio',
            options={'verbose_name_plural': 'Acessórios'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name_plural': 'Veículos'},
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.categoria'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.cor'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.marca'),
        ),
    ]
