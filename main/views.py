from django.shortcuts import render


def index(request):
    context = {
        'title': 'TechStore - Главная',
        'content': 'Магазин компьютерной техники TechStore'
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'TechStore - О нас',
        'content': 'О нас',
        'text': 'Текст о том какой классный этот интернет магазин.'
    }
    return render(request, 'main/about.html', context)
