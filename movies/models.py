from django.db import models

# Create your models here.

# Gendre
class Gender(models.Model):
    gender_description = models.CharField(max_length=10, verbose_name="Φύλο")

    def __str__(self):
        return self.gender_description

    class Meta:
        db_table = "gender"
        verbose_name = "Φύλο"
        verbose_name_plural = "Φύλα"
        ordering = ["gender_description"]


class Genre(models.Model):
    genre_description = models.CharField(max_length=100, verbose_name="Είδος Ταινίας")

    def __str__(self):
        return self.genre_description

    class Meta:
        db_table = "genre"
        verbose_name = "Είδος ταινίας"
        verbose_name_plural = "Είδη ταινιών"
        ordering = ["genre_description"]

Language_choice = {
    ('EN', 'English'),
    ('GR', 'Greek')
}

class Company(models.Model):
    company_description = models.CharField(max_length=100, verbose_name="Εταιρία Παραγωνής")

    def __str__(self):
        return self.company_description

    class Meta:
        db_table = "company"
        verbose_name = "Εταιρία Παραγωγής"
        verbose_name_plural = "Εταιρίες Παραγωγής"
        ordering = ["company_description"]


class Director(models.Model):
    director_firstName = models.CharField(max_length=100, verbose_name="Όνομα Σκηνοθέτη")
    director_lastName = models.CharField(max_length=100, verbose_name="Επώνυμο Σκηνοθέτη")
    director_dateOfBirth = models.DateField(verbose_name="Ημερομηνία γέννησης", null=True)
    director_placeOfBirth = models.CharField(max_length=30, verbose_name="Τόπος Γέννησης", null=True)
    director_gender = models.ForeignKey(Gender, on_delete=models.PROTECT, verbose_name='Φύλο')
    director_bio = models.TextField(verbose_name="Βιογραφικό/Πληροφορίες", null=True)
    image = models.ImageField(null=True, verbose_name="Φώτο Σκηνοθέτη")

    def __str__(self):
        return "{0} ({1} {2})".format(self.director_lastName, self.director_firstName, self.director_gender)

    class Meta:
        db_table = "director"
        verbose_name = "Σκηνοθέτης"
        verbose_name_plural = "Σκηνοθέτες"
        ordering = ["director_lastName"]


class Actor(models.Model):
    actor_firstName = models.CharField(max_length=100, verbose_name="Όνομα Ηθοποιού")
    actor_lastName = models.CharField(max_length=100, verbose_name="Επώνυμο Ηθοποιού")
    actor_dateOfBirth = models.DateField(verbose_name="Ημερομηνία γέννησης", null=True)
    actor_placeOfBirth = models.CharField(max_length=30, verbose_name="Τόπος Γέννησης", null=True)
    actor_gender = models.ForeignKey(Gender, on_delete=models.PROTECT, verbose_name='Φύλο')
    actor_bio = models.TextField(verbose_name="Βιογραφικό/Πληροφορίες", null=True)

    def __str__(self):
        return "{0} ({1} {2})".format(self.actor_lastName, self.actor_firstName, self.actor_gender)

    class Meta:
        db_table = "actor"
        verbose_name = "Ηθοποιός"
        verbose_name_plural = "Ηθοποιοί"
        ordering = ["actor_lastName"]

    def fullname(self):
        return self.actor_lastName + " " + self.actor_firstName


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="Τίτλος ταινίας")
    duration = models.IntegerField(null=True, verbose_name="Διάρκεια")
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='Είδος')
    language = models.CharField(choices=Language_choice, max_length=20, verbose_name="Γλώσσα", null=True)
    premiere_date = models.DateField(verbose_name="Ημερομηνία Πρεμίερας", null=True)
    url_imbd = models.CharField(max_length=300, verbose_name="Σύνδεσμος_IMBD")
    image = models.ImageField(null=True, verbose_name="Εξώφυλλο")
    poster = models.ImageField(null=True, verbose_name="Ποστερ")
    imdb_rate = models.FloatField(verbose_name="Βαθμολογία_IMBD", null=True)
    plot = models.TextField(verbose_name="Πλοκή")
    director = models.ForeignKey(Director, on_delete=models.PROTECT, verbose_name="Σκηνοθέτης")
    actors = models.ManyToManyField(Actor, related_name="movies", verbose_name="Ηθοποιοί")
    critics = models.TextField(verbose_name="Κριτικές")
    trailer = models.CharField(max_length=300, verbose_name="Trailer")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Εταιρία Παραγωγής", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ημερομηνία Δημιουργίας")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ημερομηνία Ενημέρωσης")
    views = models.IntegerField(null=True, verbose_name="Προβολες")

    def __str__(self):
        if self.premiere_date == None:
            return self.title + " " + "duration:" + str(self.duration)
        else:
            return self.title + " " + "duration:" + str(
                self.duration) + " " + "Premiere Date:" + self.premiere_date.strftime("%d/%m/%Y")

    class Meta:
        db_table = "Movie"
        verbose_name = "Ταινία"
        verbose_name_plural = "Ταινίες"
        ordering = ["title"]

    def get_actors_str(self):
        actors_str = ""
        actors = self.actors.all()
        for actor in actors:
            actors_str += actor.fullname() + ", "
        return actors_str[:-2]

class Contact(models.Model):
    subject=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return "{0} ({1} {2})".format(self.subject, self.email, self.message)

    class Meta:
        db_table = "Contact"
        verbose_name = "Επικοινωνία"
        verbose_name_plural = "Επικοινωνία"
        ordering = ["subject"]
