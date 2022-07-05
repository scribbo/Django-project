from django import template

register = template.Library()

@register.simple_tag
def disabled_if_cannot_buy(user, product):
    if user.is_anonymous:
        return 'disabled'
        
    if product.quantity == 0:
        return 'disabled'
    
    basket_item = user.basket.filter(product=product).first()
    if basket_item and basket_item.quantity >= product.quantity:
        return 'disabled'
    
    return ''
