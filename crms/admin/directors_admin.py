from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import DirectorDetails, Directors

class DirectorDetailsInline(ModelAdminMixin, admin.TabularInline):
    model = DirectorDetails
    extra = 3

    fieldsets = (
        (None, {
            'fields': ('directors',
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
                       'email',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )

class DirectorsAdmin(ModelAdminMixin, admin.ModelAdmin):
    
    inlines = [DirectorDetailsInline]

    fieldsets = (
        (None, {
            'fields': ('cipa_id',)},
         ),
        audit_fieldset_tuple
    )

admin.site.register(Directors, DirectorsAdmin)

