# Generated by Django 3.2 on 2021-04-09 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='jop_type',
            field=models.CharField(choices=[('full time', 'full time'), ('part time', 'part time')], default='', max_length=30),
            preserve_default=False,
        ),
    ]
