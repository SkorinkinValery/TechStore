from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from goods.models import Product


def catalog(request, category_slug):
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    page = request.GET.get('page', 1)

    if category_slug == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__slug=category_slug)

    if on_sale:
        products = products.filter(discount__gt=0)

    if order_by and order_by != 'default':
        products = products.order_by(order_by)

    paginator = Paginator(products, 3)
    current_page = paginator.page(page)

    context = {
        'title': 'TechStore - Каталог',
        'products': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    context = {
        'title': 'TechStore - Товар',
        'product': product
    }
    return render(request, 'goods/product.html', context)
