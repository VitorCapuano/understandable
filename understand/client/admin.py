from django.contrib import admin

from client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpf',)
    pass

admin.site.register(Client, ClientAdmin)
