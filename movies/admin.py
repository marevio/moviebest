from django.contrib import admin
from .models import Genre,Director,Movie,Actor,Company, Gender

# Register your models here.
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Company)
admin.site.register(Gender)