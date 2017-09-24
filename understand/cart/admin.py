from django.contrib import admin

from cart.models import Cart, CartProducts


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'id',)


class CartProductAdmin(admin.ModelAdmin):
    list_display = ('cart',)


admin.site.register(Cart, CartAdmin)
admin.site.register(CartProducts, CartProductAdmin)
