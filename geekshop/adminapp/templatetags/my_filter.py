from django import template

register = template.Library()

@register.filter
def stars(value):
    return f'***{value}***'
