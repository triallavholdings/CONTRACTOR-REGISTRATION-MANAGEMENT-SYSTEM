from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import Shareholders, ShareholderDetails

class ShareholderDetailsInline(ModelAdminMixin, admin.TabularInline):
    model = ShareholderDetails
    extra = 3

    fieldsets = (
        (None, {
            'fields': ('shareholders',
                       'first_name',
                       'middle_name',
                       'last_name',
                       'gender',
                       'dob',
                       'nationality',
                       'omang',
                       'expiry_date',
                       'passport_number',
                       'work_permit',
                       'percentage_shares',
                       'gov_employee',
                       'email',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )

class ShareholdersAdmin(ModelAdminMixin, admin.ModelAdmin):
    
    inlines = [ShareholderDetailsInline]

    fieldsets = (
        (None, {
            'fields': ('cipa_id',)},
         ),
        audit_fieldset_tuple
    )

admin.site.register(Shareholders, ShareholdersAdmin)

