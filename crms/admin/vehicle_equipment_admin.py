from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import (
    VehicleEquipment, Vehicle, PlantEquipment, OfficeEquipments)

class VehicleInline(ModelAdminMixin, admin.TabularInline):
    model = Vehicle
    extra = 3

    fieldsets = (
        (None, {
            'fields': ('vehicle_equipment',
                       'registered_owner',
                       'ownership',
                       'registration_no',
                       'first_reg_date',
                       'make_model',
                       'prev_owner',
                       'description',
                       'present_value',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )


class PlantEquipmentInline(ModelAdminMixin, admin.TabularInline):
    model = PlantEquipment
    extra = 3

    fieldsets = (
        (None, {
            'fields': ('vehicle_equipment',
                       'owner_name',
                       'ownership',
                       'registration_no',
                       'date_of_purchase',
                       'description',
                       'present_value',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )


class OfficeEquipmentsInline(ModelAdminMixin, admin.TabularInline):
    model = OfficeEquipments
    extra = 3

    fieldsets = (
        (None, {
            'fields': ('vehicle_equipment',
                       'office_furniture',
                       'present_value',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )


class VehicleEquipmentAdmin(ModelAdminMixin, admin.ModelAdmin):
    
    inlines = [
        VehicleInline,
        PlantEquipmentInline,
        OfficeEquipmentsInline]

    fieldsets = (
        (None, {
            'fields': ('asserts_value',
                       'equipment_value',
                       'capital',
                       'total_employees')},
         ),
        audit_fieldset_tuple
    )

admin.site.register(VehicleEquipment, VehicleEquipmentAdmin)
