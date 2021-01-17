from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as logins, logout ,authenticate
from django.utils import timezone
from .models import Movie

# Create your views here.

# Home
def home(request):
    return render(request, 'movies/home.html')

# About us
def aboutus(request):
    return render(request, 'movies/aboutus.html')

# Register
def Register(request):
    if request.method == 'POST':
        Register_form = UserCreationForm(request.POST)
        if Register_form.is_valid():
            user = Register_form.save()
            logins(request, user)
            return redirect('home.html')
    else:
        Register_form = UserCreationForm()
    return render(request, 'movies/Register.html',{'Register_form':Register_form})

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


#login
def login(request):
    if request.method == 'POST':
        Login_form = AuthenticationForm(data=request.POST)
        if Login_form.is_valid():
            return redirect('movies/home.html')
    else:
        Login_form = AuthenticationForm()

    return render(request,'movie/login.html',{'Login_form':Login_form})