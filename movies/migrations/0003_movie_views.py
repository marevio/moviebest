# Generated by Django 2.2.2 on 2021-01-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210128_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='views',
            field=models.IntegerField(null=True, verbose_name='Προβολες'),
        ),
    ]
