from django.shortcuts import render, redirect

from goods.models import Products
from .models import Cart

def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)



    return redirect(request.META["HTTP_REFERER"])

def cart_change(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                if cart.quantity > 1:
                    cart.quantity += -1
                    cart.save()
                else:
                    cart = Cart.objects.get(id=cart.id)
                    cart.delete()
    return redirect(request.META["HTTP_REFERER"])



def cart_remove(request, product_slug):
    cart = Cart.objects.get(slug=product_slug)
    cart.delete()

    return redirect(request.META["HTTP_REFERER"])

