from django.contrib import admin
from .models import Genre,Director,Movie,Actor,Company

# Register your models here.
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Company)