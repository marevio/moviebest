from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as logins, logout, authenticate
from django.utils import timezone
from .models import Movie, Contact
from movies import models
from django.contrib.auth.decorators import login_required
from .Register_form import Register_form
from django.db.models import Q
# Create your views here.


# Home
def home(request):
    Movies_obj = models.Movie.objects.all()
    Movies_obj_Created = models.Movie.objects.order_by('created_at')
    Movies_obj_Watched = models.Movie.objects.order_by('views')
    return render(request, 'movies/mainView.html', {'movies': Movies_obj, 'moviesCreated': Movies_obj_Created, 'moviesViews': Movies_obj_Watched} )

# About us
def aboutus(request):
    return render(request, 'movies/aboutus.html')

# Contact
def contact(request):
    if request.method=="POST":
        contact=Contact()
        subject=request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.subject=subject
        contact.email=email
        contact.message=message
        contact.save()
        return render(request, 'movies/contactMessage.html')
        #return HttpResponse()
    return render(request, 'movies/contact.html')

# Register
def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = Register_form()

        if request.method == 'POST':
            form = Register_form(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form' : form}
        return  render(request, 'movies/Register.html', context)

#login
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                logins(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'movies/login.html', context)


#logout
def logoutUser(request):
    logout(request)
    return redirect('home')

#movies
def adv_Search(request):
    txt = request.GET.get('txt', '')

    if txt != '':
        #posts = models.Movie.objects.filter(plot__contains=txt)
        posts = models.Movie.objects.filter(Q(title__contains=txt) | Q(plot__contains=txt) | Q(actors__actor_lastName__contains=txt) | Q(director__director_lastName__contains=txt)).distinct()
    else:
        posts = models.Movie.objects.all()

    return render(request, 'movies/adv_search.html', {'movies': posts})

#movie detail
@login_required(login_url='login')
def detail(request, movie_id):
    get_movie = models.Movie.objects.get(title=movie_id)
    return render(request, 'movies/detail.html', {'home_movie': get_movie})

#movie language Search
@login_required(login_url='login')
def search(request, movie_id):
    get_movie = models.Movie.objects.filter(language=movie_id)
    return render(request, 'movies/search.html', {'home_movie': get_movie.all()})

#movie genre Search
@login_required(login_url='login')
def search_2(request, movie_id):
    get_movie = models.Movie.objects.filter(genre__genre_description=movie_id)
    return render(request, 'movies/search_2.html', {'home_movie': get_movie.all()})

@login_required(login_url='login')
def director(request, movie_id):
    get_movie = models.Movie.objects.filter(director__director_lastName__contains=movie_id)
    return render(request, 'movies/director.html', {'home_movie': get_movie})