from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import (
    Employees, SeniorPermenantStaffBW,
    SeniorPermenantStaffForeigner)


class SeniorPermenantStaffBWInline(ModelAdminMixin, admin.TabularInline):
    model = SeniorPermenantStaffBW
    extra = 3

    fieldsets = (
        (None, {
            'fields': ('employees',
                       'first_name',
                       'middle_name',
                       'last_name',
                       'omang',
                       'dob',
                       'profession_trade',
                       'position',
                       'qualification',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )



class SeniorPermenantStaffForeignerInline(ModelAdminMixin, admin.TabularInline):
    model = SeniorPermenantStaffForeigner
    extra = 3

    fieldsets = (
        (None, {
            'fields': ('employees',
                       'first_name',
                       'middle_name',
                       'last_name',
                       'dob',
                       'passport_number',
                       'work_permit',
                       'expiry_date',
                       'profession_trade',
                       'position',
                       'qualification',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )



class EmployeesAdmin(ModelAdminMixin, admin.ModelAdmin):
    
    inlines = [
        SeniorPermenantStaffBWInline,
        SeniorPermenantStaffForeignerInline]

    fieldsets = (
        (None, {
            'fields': ('cipa_id',
                       'bw_employees',
                       'other_nationalities',
                       'total_employees')},
         ),
        audit_fieldset_tuple
    )


admin.site.register(Employees, EmployeesAdmin)
