from django.contrib import admin

from partner.models import Partner


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'social_reason',)
    pass

admin.site.register(Partner, PartnerAdmin)
