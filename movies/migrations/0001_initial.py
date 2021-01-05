# Generated by Django 2.0 on 2021-01-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_description', models.CharField(max_length=100, verbose_name='Είδος Ταινίας')),
            ],
            options={
                'verbose_name': 'Είδος ταινίας',
                'verbose_name_plural': 'Είδη ταινιών',
                'db_table': 'genre',
                'ordering': ['genre_description'],
            },
        ),
    ]