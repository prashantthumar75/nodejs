# Generated by Django 3.1 on 2020-08-30 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_registermodel_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registermodel',
            name='num',
        ),
    ]
