# Generated by Django 3.1.5 on 2021-01-04 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_firstName', models.CharField(max_length=100, verbose_name='Όνομα Ηθοποιού')),
                ('actor_lastName', models.CharField(max_length=100, verbose_name='Επώνυμο Ηθοποιού')),
                ('actor_dateOfBirth', models.DateField(verbose_name='Ημερομηνία γέννησης')),
                ('actor_placeOfBirth', models.CharField(max_length=30, verbose_name='Τόπος Γέννησης')),
                ('actor_gender', models.CharField(max_length=20, verbose_name='Γένος')),
                ('actor_bio', models.CharField(max_length=300, verbose_name='Βιογραφικό/Πληροφορίες')),
            ],
            options={
                'verbose_name': 'Ηθοποιός',
                'verbose_name_plural': 'Ηθοποιοί',
                'db_table': 'actor',
                'ordering': ['actor_lastName'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_description', models.CharField(max_length=100, verbose_name='Εταιρία Παραγωνής')),
            ],
            options={
                'verbose_name': 'Εταιρία Παραγωγής',
                'verbose_name_plural': 'Εταιρίες Παραγωγής',
                'db_table': 'company',
                'ordering': ['company_description'],
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_firstName', models.CharField(max_length=100, verbose_name='Όνομα Σκηνοθέτη')),
                ('director_lastName', models.CharField(max_length=100, verbose_name='Επώνυμο Σκηνοθέτη')),
                ('director_dateOfBirth', models.DateField(verbose_name='Ημερομηνία γέννησης')),
                ('director_placeOfBirth', models.CharField(max_length=30, verbose_name='Τόπος Γέννησης')),
                ('director_gender', models.CharField(max_length=20, null=True, verbose_name='Γένος')),
                ('director_bio', models.TextField(verbose_name='Βιογραφικό/Πληροφορίες')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Φώτο Σκηνοθέτη')),
            ],
            options={
                'verbose_name': 'Σκηνοθέτης',
                'verbose_name_plural': 'Σκηνοθέτες',
                'db_table': 'director',
                'ordering': ['director_lastName'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Τίτλος ταινίας')),
                ('duration', models.IntegerField(null=True, verbose_name='Διάρκεια')),
                ('premiere_date', models.DateField(verbose_name='Ημερομηνία Πρεμίερας')),
                ('url_imbd', models.CharField(max_length=300, verbose_name='Σύνδεσμος_IMBD')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Εξώφυλλο')),
                ('imdb_rate', models.CharField(max_length=20, verbose_name='Βαθμολογία_IMBD')),
                ('plot', models.TextField(verbose_name='Πλοκή')),
                ('critics', models.TextField(verbose_name='Κριτικές')),
                ('trailer', models.CharField(max_length=300, verbose_name='Trailer')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ημερομηνία Δημιουργίας')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ημερομηνία Ενημέρωσης')),
                ('actors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actor', verbose_name='Ηθοποιοί')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.company', verbose_name='Εταιρία Παραγωγής')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.director', verbose_name='Σκηνοθέτης')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='Είδος')),
            ],
            options={
                'verbose_name': 'Ταινία',
                'verbose_name_plural': 'Ταινίες',
                'db_table': 'Movie',
                'ordering': ['title'],
            },
        ),
    ]