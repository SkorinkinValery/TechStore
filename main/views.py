from django.shortcuts import render

from goods.models import Category


def index(request):
    categories = Category.objects.all()

    context = {
        'title': 'TechStore - Главная',
        'content': 'Магазин компьютерной техники TechStore',
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'TechStore - О нас',
        'content': 'О нас',
        'text': 'Текст о том какой классный этот интернет магазин.'
    }
    return render(request, 'main/about.html', context)
