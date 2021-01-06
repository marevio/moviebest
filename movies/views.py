from django.shortcuts import render

# Create your views here.

# Home
def home(request):
    return render(request, 'movies/home.html')

# About us
def aboutus(request):
    return render(request, 'movies/aboutus.html')