from django.shortcuts import render, get_object_or_404
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


def category(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=pk)
    products = Products.objects.filter(category=category)
    return render(
        request, 
        'mainapp/category.html', 
        context ={
        'title': 'Каталог',
        'menu': menu_links,
        'products': products,
        'category': category,
        'categories': categories,
        }
    )


def contact(request): 
    return render(request, 'mainapp/contact.html', context ={
        'title': 'Контакты',
        'menu': menu_links,
    }) 