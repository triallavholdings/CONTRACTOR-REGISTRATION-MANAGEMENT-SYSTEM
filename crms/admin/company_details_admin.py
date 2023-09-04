from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import CompanyDetail


@admin.register(CompanyDetail)
class CompanyDetailAdmin(ModelAdminMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('local_provider',
                       'business_type',
                       'name',
                       'cipa_registration',
                       'cipa_id',
                       'registration_date',
                       'ownership',
                       'webpage')},
         ),
        audit_fieldset_tuple
    )
