from django.contrib.auth import get_user_model
from mainapp.models import Products
from django.db import models, transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver


class OrderItemManager(models.Manager):
    def quantity(self):
        return sum([item.quantity for item in self.all()])

    def sum(self):
        return sum([item.product.price * item.quantity for item in self.all()])


class Order(models.Model):
    CREATED = 'CREATED'
    PAID = 'PAID'
    SENT = 'SENT'
    DELIVERED = 'DELIVERED'  
    CANCELLED = 'CANCELLED'



    STATUS_CHOICES= ( 
        (CREATED, 'Создан'), 
        (PAID, 'Оплачен'),
        (SENT, 'Отправлен'),
        (DELIVERED, 'Доставлен'),  
        (CANCELLED, 'Отменен'), 
        ) 
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='orders'
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=CREATED)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def can_pay(self):
        return self.status == Order.CREATED
    
    @property
    def can_cancel(self):
        return self.status in [Order.CREATED, Order.PAID, Order.SENT] 


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='basket'
        )
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    
    objects = OrderItemManager()

    @property
    def cost(self):
        return self.quantity * self.product.price


    def __str__(self):
        return f'{self.product} - {self.quantity} шт.'
    
    '''@transaction.atomic
    def save(self, *args, **kwargs):
        old_order_item = OrderItem.objects.filter(pk=self.pk).first()
        if old_order_item:
            quantity_delta = self.quantity - old_order_item.quantity
            self.product.quantity += quantity_delta
            
        else:
            self.product.quantity -= self.quantity
        
        self.product.save()
        return super().save(*args, **kwargs)'''
    

@receiver(pre_save, sender=OrderItem)
def update_product_quantity(sender, instance, **kwargs):
    old_order_item = OrderItem.objects.filter(pk=instance.pk).first()
    if old_order_item:
        quantity_delta = instance.quantity - old_order_item.quantity
        instance.product.quantity -= quantity_delta
        
    else:
        instance.product.quantity -= instance.quantity
    
    instance.product.save()

    


