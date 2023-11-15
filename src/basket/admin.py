from django.contrib import admin

# Register your models here.
from . import models

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user',
        'summ',
        'order_book',
        'currency'
    ]
admin.site.register(models.Order, OrderAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'good_quantity',
        'total_price', 
        'created'
    ]

class GoodInCartAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'cart',
        'good',
        'quantity',
        'price',
        'total_price'
    ]

admin.site.register(models.GoodInCart, GoodInCartAdmin)
admin.site.register(models.Cart, CartAdmin)    