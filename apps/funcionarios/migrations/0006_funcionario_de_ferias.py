# Generated by Django 3.1.2 on 2020-11-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0005_funcionario_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='de_ferias',
            field=models.BooleanField(default=False),
        ),
    ]
