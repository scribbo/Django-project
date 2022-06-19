from requests import request


def menu_links(request):
    return {
        'menu': {
            'index': 'Магазин',
            'products': 'Каталог',
            'contact': 'Контакты',
        }
    }
