from django.contrib import admin

from ..models import BankerDetails


@admin.register(BankerDetails)
class BankerDetailsAdmin(admin.ModelAdmin):
    pass