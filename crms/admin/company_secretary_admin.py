from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import (
    CompanySecretary, PhysicalAddress, PostalAddress)

class PhysicalAddressInline(ModelAdminMixin, admin.TabularInline):
    model = PhysicalAddress
    extra = 3
    
    fieldsets = (
        (None, {
            'fields': ('secretary',
                       'plot',
                       'street',
                       'village_town_city')},
         ),
        audit_fieldset_tuple
    )


class PostalAddressInline(ModelAdminMixin, admin.TabularInline):
    model = PostalAddress
    extra = 3
    
    fieldsets = (
        (None, {
            'fields': ('secretary',
                       'box_private_no',
                       'number',
                       'address_line',
                       'address_line2',
                       'address_line3',
                       'country',
                       'village_town_city')},
         ),
        audit_fieldset_tuple
    )


class CompanySecretaryAdmin(ModelAdminMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('name',
                       'home_phone',
                       'bus_phone',
                       'mobile_no',
                       'email',
                       'nationality',
                       'omang',
                       'expiry_date')},
         ),
        audit_fieldset_tuple
    )
    
    inlines = [
        PostalAddressInline,
        PhysicalAddressInline]

admin.site.register(CompanySecretary, CompanySecretaryAdmin)

