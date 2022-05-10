from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from numpy import imag
from .models import Basket
from mainapp.models import Products


def view (request):
    return render(request, 'basketapp/view.html', context ={
        'basket': Basket.objects.filter(user=request.user)
    })


def add (request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)
    if basket:
        basket_item = basket[0]
        basket_item.quantity += 1
        basket_item.save()
    else:
        basket_item = Basket(user=request.user, product=product)
        basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse ('index')))


def remove (request, basket_id):
    basket = get_object_or_404(Basket, pk=basket_id)
    basket.quantity -= 1
    if not basket.quantity:
        basket.delete()
    else:
        basket.save()
    return HttpResponseRedirect(reverse ('basket:view'))

