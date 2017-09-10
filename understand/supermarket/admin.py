from django.contrib import admin

from supermarket.models import Supermarket


class SupermarketAdmin(admin.ModelAdmin):
    pass

admin.site.register(Supermarket, SupermarketAdmin)
