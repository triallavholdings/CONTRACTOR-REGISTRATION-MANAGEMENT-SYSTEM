from django.contrib import admin

from ..models import CompanyAddress


@admin.register(CompanyAddress)
class CompanyAddressAdmin(admin.ModelAdmin):
    pass