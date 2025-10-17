from django.shortcuts import render

from goods.models import Product


def catalog(request):
    products = Product.objects.all()

    context = {
        'title': 'TechStore - Каталог',
        'products': products
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    context = {
        'title': 'TechStore - Товар'
    }
    return render(request, 'goods/product.html', context)
