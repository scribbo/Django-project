from django.urls import reverse
from django.shortcuts import render

menu_links = {
    'index': 'Магазин',
    'products': 'Каталог',
    'contact': 'Контакты'
}


def main(request): 
    return render(request, 'mainapp/index.html', context ={
        'title': 'Магазин',
        'menu': menu_links,
    }) 


def products(request): 
    return render(request, 'mainapp/products.html', context ={
        'title': 'Каталог',
        'menu': menu_links,
        'products': [
            {'name': 'Стул_1', 'description': 'Стул повышенного качества', 'image': 'img/product-11.jpg'},
            {'name': 'Стул_2', 'description': 'Прекрасный стул', 'image': 'img/product-21.jpg'},
            {'name': 'Стул_3', 'description': 'Стул премиального качества', 'image': 'img/product-31.jpg'},
        ]
    }) 


def contact(request): 
    return render(request, 'mainapp/contact.html', context ={
        'title': 'Контакты',
        'menu': menu_links,
    }) 