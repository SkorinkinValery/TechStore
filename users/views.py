from django.shortcuts import render


def register(request):
    return render(request, 'users/registration.html', {})


def login(request):
    return render(request, 'users/login.html', {})


def logout(request):
    ...


def profile(request):
    return render(request, 'users/profile.html', {})
