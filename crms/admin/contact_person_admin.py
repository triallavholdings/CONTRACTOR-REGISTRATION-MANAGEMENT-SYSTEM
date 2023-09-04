from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import PrimaryContactPerson, SecondaryContactPerson


@admin.register(PrimaryContactPerson)
class PrimaryContactPersonAdmin(ModelAdminMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('cipa_id',
                       'first_name',
                       'middle_name',
                       'last_name',
                       'dob',
                       'email',
                       'cell_phone',
                       'tel_phone',
                       'business_phone',
                       'nationality',
                       'omang',
                       'expiry_date')},
         ),
        audit_fieldset_tuple
    )


@admin.register(SecondaryContactPerson)
class SecondaryContactPersonAdmin(ModelAdminMixin, admin.ModelAdmin):
    
    fieldsets = (
        (None, {
            'fields': ('cipa_id',
                       'first_name',
                       'middle_name',
                       'last_name',
                       'dob',
                       'email',
                       'cell_phone',
                       'tel_phone',
                       'business_phone',
                       'nationality',
                       'omang',
                       'expiry_date')},
         ),
        audit_fieldset_tuple
    )
