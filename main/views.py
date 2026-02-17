from django.shortcuts import render


def index(request):
    context = {
        'title': 'TechStore - Главная',
        'content': 'Магазин компьютерной техники TechStore',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'TechStore - О нас',
        'content': 'О нас',
        'text': 'Текст о том какой классный этот интернет магазин.'
    }
    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        'title': 'TechStore - Контакты',
        'content': 'Контакты',
        'text': 'Здесь должны располагаться контакты нашего магазина.'
    }
    return render(request, 'main/contacts.html', context)

def delivery_payment(request):
    context = {
        'title': 'TechStore - Доставка и оплата',
        'content': 'Доставка и оплата',
        'text': 'Здесь должна располагаться информация о доставке и оплате нашего магазина.'
    }
    return render(request, 'main/delivery_payments.html', context)