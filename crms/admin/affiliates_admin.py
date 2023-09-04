from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import Affiliates


@admin.register(Affiliates)
class AffiliatesAdmin(ModelAdminMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('affiliate',
                       'address',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )
