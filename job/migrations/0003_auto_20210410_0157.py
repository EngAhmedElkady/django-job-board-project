# Generated by Django 3.2 on 2021-04-09 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_jop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='job',
            name='published',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=5000),
        ),
    ]
