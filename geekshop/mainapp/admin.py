from django.contrib import admin
from .models import Category, Products


@ admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@ admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    pass
