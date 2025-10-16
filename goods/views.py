from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'TechStore - Каталог'
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    context = {
        'title': 'TechStore - Товар'
    }
    return render(request, 'goods/product.html', context)
