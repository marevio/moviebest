from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login , logout ,authenticate
from django.utils import timezone
from .models import Movie


# Create your views here.
from .Register_form import Register_form


# Home
def home(request):
    return render(request, 'movies/home.html')

# About us
def aboutus(request):
    return render(request, 'movies/aboutus.html')

# Register
def Register(request):
    form = Register_form()

    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form' : form}
    return  render(request, 'movies/Register.html', context)

#login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('movies/home.html')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'movie/login.html', context)

#logout
def logoutUser(request):
    logout(request)
    return redirect(request, 'movie/login.html')

#movies
def movie_list(request):
    cat=request.GET.get('cat','')
    txt=request.GET.get('txt','')
    try:
        cat=int(cat)
    except:
        cat=False
    if cat is False:
        if txt == '':
            posts = Movie.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        else:
            posts = Movie.objects.filter(published_date__lte=timezone.now()).filter(text__contains=txt).order_by('published_date')
    else:
        posts = Movie.objects.filter(published_date__lte=timezone.now()).filter(category=cat).order_by('published_date')
    return render(request, 'movies/movie_list.html', {'movies': posts})

def movie_detail(request, pk):
    post = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': post})