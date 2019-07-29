from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm, RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def my_movies(request):
    if request.user.is_anonymous:
        messages.warning(request, 'You have to be logged in!')
        return redirect('login')

    context = {
        "movies": request.user.movies.all(),
        "movies": Movie.objects.filter(added_by=request.user),
    }
    return render(request, 'list.html', context)


def user_logout(request):
    logout(request)
    messages.warning(request, 'We\'re sorry to see you go!')
    return redirect('login')

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            my_username = form.cleaned_data['username']
            my_password = form.cleaned_data['password']
            user_obj = authenticate(username=my_username, password=my_password)
            if user_obj is not None:
                login(request, user_obj)
                messages.success(request, 'Welcome Back!')
                return redirect('movies')
            messages.warning(request, 'Incorrect username/password!')
    context = {
        "login_form": form,
    }
    return render(request, 'login.html', context)

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('movies')
    context = {
        "register_form": form,
    }
    return render(request, 'register.html', context)

def create_movie(request):
    if request.user.is_anonymous:
        messages.warning(request, 'You have to be logged in!')
        return redirect('login')
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie_obj = form.save(commit=False)
            movie_obj.added_by = request.user
            movie_obj.save()
            form.save_m2m()
            return redirect('movies')
    context = {
        "create_form": form,
    }
    return render(request, 'create.html', context)

def movie_list(request):
    context = {
        "movies": Movie.objects.all(),
    }
    return render(request, 'list.html', context)


def movie_detail(request, movie_id):
    context = {
        "movie": Movie.objects.get(id=movie_id),
    }
    return render(request, 'detail.html', context)
