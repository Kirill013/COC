# Generated by Django 3.2.18 on 2023-04-04 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230405_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='doe',
            new_name='DOE',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='issn',
            new_name='ISSN',
        ),
    ]
