# Generated by Django 3.1.2 on 2020-10-20 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_antiga', '0003_auto_20201020_0726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrousuarios',
            old_name='name',
            new_name='nome',
        ),
    ]
