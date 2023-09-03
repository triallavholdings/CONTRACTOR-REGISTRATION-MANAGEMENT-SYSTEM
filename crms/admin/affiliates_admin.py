from django.contrib import admin

from ..models import Affiliates


@admin.register(Affiliates)
class AffiliatesAdmin(admin.ModelAdmin):
    pass