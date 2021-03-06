# Generated by Django 2.1 on 2018-08-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180811_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assessment_practices',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a your course description', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='grading_policy',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='objectives',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='projects',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='resources',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='content_objectives',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='language_objectives',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='lesson_outline',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='resources',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
