# Generated by Django 2.1.2 on 2020-09-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0003_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='utilizada',
            field=models.BooleanField(default=False),
        ),
    ]
