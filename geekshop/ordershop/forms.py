from django import forms
from .models import Order, OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ('order',)

OrderItemFormset = forms.inlineformset_factory(Order, OrderItem, OrderItemForm, extra=2)