# Generated by Django 3.1 on 2020-08-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0004_remove_registermodel_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='registermodel',
            name='num',
            field=models.IntegerField(default=1, verbose_name='number'),
            preserve_default=False,
        ),
    ]
