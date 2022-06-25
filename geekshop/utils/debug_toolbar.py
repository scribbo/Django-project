from debug_toolbar.middleware import show_toolbar

def show_debug_toolbar(request):
    return show_toolbar or bool(request.GET.get('debug', False))