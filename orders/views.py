from django.shortcuts import redirect
from django.contrib import messages

from carts.models import Cart
from orders.models import Order, OrderItem


def order_add(request):
    cart_items = Cart.objects.filter(user_id=request.user.id)
    if not cart_items.exists():
        messages.error(request, 'Корзина пуста')
        return redirect('users:user_cart')

    order = Order.objects.create(user_id=request.user.id)

    for cart_item in cart_items:
        OrderItem.objects.create(product_id=cart_item.product_id, quantity=cart_item.quantity, order_id=order.id)
    cart_items.delete()
    return redirect('users:profile')


def order_update_status():
    pass
