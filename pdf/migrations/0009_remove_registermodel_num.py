# Generated by Django 3.1 on 2020-10-11 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0008_auto_20201011_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registermodel',
            name='num',
        ),
    ]