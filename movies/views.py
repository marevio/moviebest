from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as logins

# Create your views here.

# Home
def home(request):
    return render(request, 'movies/home.html')

# About us
def aboutus(request):
    return render(request, 'movies/aboutus.html')

# Register
def Register(request):
    if request.method == 'post':
        Register_form = UserCreationForm(request.POST)
        if Register_form.is_valid():
            user = Register_form.save()
            logins(request, user)
            return redirect('movies/home.html')
    else:
        Register_form = UserCreationForm()
    return render(request, 'movies/Register.html',{'Register_form':Register_form})

#login
def login(request):
    if request.method == 'POST':
        Login_form = AuthenticationForm(data=request.POST)
        if Login_form.is_valid():
            return redirect('movies/home.html')
    else:
        Login_form = AuthenticationForm()

    return render(request,'movie/login.html',{'Login_form':Login_form})