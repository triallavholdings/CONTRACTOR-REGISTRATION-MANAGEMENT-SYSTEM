from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import CompanyAddress


@admin.register(CompanyAddress)
class CompanyAddressAdmin(ModelAdminMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('cipa_id',
                       'country',
                       'district',
                       'village_town',
                       'plot_unit',
                       'street_ward',
                       'postal',
                       'box_number')},
         ),
        audit_fieldset_tuple
    )
