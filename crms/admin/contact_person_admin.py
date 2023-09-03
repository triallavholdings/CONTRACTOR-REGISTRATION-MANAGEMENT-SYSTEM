from django.contrib import admin

from ..models import PrimaryContactPerson, SecondaryContactPerson


@admin.register(PrimaryContactPerson)
class PrimaryContactPersonAdmin(admin.ModelAdmin):
    pass


@admin.register(SecondaryContactPerson)
class SecondaryContactPersonAdmin(admin.ModelAdmin):
    pass