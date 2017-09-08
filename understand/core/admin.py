from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    pass


class SupermarketAdmin(admin.ModelAdmin):
    pass


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Supermarket, SupermarketAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart, CartAdmin)
