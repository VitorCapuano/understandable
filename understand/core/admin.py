from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    pass


class SupermarketAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Supermarket, SupermarketAdmin)
admin.site.register(Category, CategoryAdmin)
