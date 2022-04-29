from django.urls import reverse
from django.shortcuts import render
from .models import Products, Category

menu_links = {
    'index': 'Магазин',
    'products': 'Каталог',
    'contact': 'Контакты',
}


def main(request): 
    return render(request, 'mainapp/index.html', context ={
        'title': 'Магазин',
        'menu': menu_links,
    }) 


def products(request):
    categories = Category.objects.all()
    products = Products.objects.all()[:3]
    return render(
        request, 
        'mainapp/products.html', 
        context ={
        'title': 'Каталог',
        'menu': menu_links,
        'products': products,
        'categories': categories,
        }
    )


def contact(request): 
    return render(request, 'mainapp/contact.html', context ={
        'title': 'Контакты',
        'menu': menu_links,
    }) 