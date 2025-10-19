from django.shortcuts import render

from goods.models import Product


def catalog(request):
    products = Product.objects.all()

    context = {
        'title': 'TechStore - Каталог',
        'products': products
    }
    return render(request, 'goods/catalog.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        'title': 'TechStore - Товар',
        'product': product
    }
    return render(request, 'goods/product.html', context)
