from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import BankerDetails


@admin.register(BankerDetails)
class BankerDetailsAdmin(ModelAdminMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('bank_name',
                       'branch',
                       'branch_code',
                       'account',
                       'account_type',
                       'swift_code',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )
