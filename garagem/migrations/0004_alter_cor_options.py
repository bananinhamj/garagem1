# Generated by Django 4.1.7 on 2023-03-28 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0003_acessorio_cor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name_plural': 'Cores'},
        ),
    ]