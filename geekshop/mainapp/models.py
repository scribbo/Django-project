from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to='product_img')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.name}'
    