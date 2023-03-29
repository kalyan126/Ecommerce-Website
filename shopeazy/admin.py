from django.contrib import admin
from .models import User, Product, Cart, CartOrder, CartOrderItems

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(CartOrder)
admin.site.register(CartOrderItems)
admin.site.register(Cart)
