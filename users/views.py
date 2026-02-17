from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from users.forms import UserRegisterForm, ProfileForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = UserRegisterForm()

    context = {
        'title': 'TechStore - Регистрация',
        'form': form
    }

    return render(request, 'users/registration.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main:index')
    else:
        form = AuthenticationForm()

    context = {
        'title': 'TechStore - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('main:index')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST or None, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные изменены успешно')
            return redirect('user:profile')
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'TechStore - Личный кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)


def user_cart(request):
    return render(request, 'users/user-cart.html')
