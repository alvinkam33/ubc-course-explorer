# Generated by Django 3.1.1 on 2021-01-01 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursetracker', '0004_auto_20210101_0142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='link',
            new_name='course_link',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='professors',
            new_name='professors_info',
        ),
    ]
