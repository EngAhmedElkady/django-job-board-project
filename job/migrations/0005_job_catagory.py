# Generated by Django 3.2 on 2021-04-10 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Catagory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.catagory'),
            preserve_default=False,
        ),
    ]
