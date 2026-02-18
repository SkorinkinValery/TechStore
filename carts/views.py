from django.shortcuts import render, redirect

from carts.models import Cart



def cart_add(request, product_id, quantity=1):
    try:
        Cart.objects.get(user_id=request.user.id, product_id=product_id)
    except Cart.DoesNotExist:
        Cart.objects.create(user_id=request.user.id, product_id=product_id,
                            quantity=quantity, session_key=request.session.session_key)
        return redirect('users:user_cart')

    return redirect('carts:cart_update', product_id)


def cart_update(request, product_id):
    cart_item = Cart.objects.get(user_id=request.user.id, product_id=product_id)
    action = request.POST.get('action')
    print(action)
    if action == 'increment':
        cart_item.quantity += 1
    else:
        cart_item.quantity -= 1
    cart_item.save()
    return redirect('users:user_cart')


def cart_delete(request, product_id):
    cart_item = Cart.objects.filter(user_id=request.user.id, product_id=product_id)
    cart_item.delete()
    return redirect('users:user_cart')
