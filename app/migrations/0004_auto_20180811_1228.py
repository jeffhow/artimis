# Generated by Django 2.1 on 2018-08-11 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180811_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonplan',
            old_name='resource_links',
            new_name='resources',
        ),
    ]