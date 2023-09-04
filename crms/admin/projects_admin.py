from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin import ModelAdminMixin
from ..models import (
    Projects, CompletedProject, OnGoingProject)

class CompletedProjectInline(ModelAdminMixin, admin.TabularInline):
    model = CompletedProject
    extra = 3

    fieldsets = (
        (None, {
            'fields': ('projects',
                       'name',
                       'details',
                       'client',
                       'client_representation',
                       'contact_number',
                       'date_completed',
                       'locality',
                       'contract_value',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )


class OnGoingProjectInline(ModelAdminMixin, admin.TabularInline):
    model = OnGoingProject
    extra = 3

    fieldsets = (
        (None, {
            'fields': ('projects',
                       'name',
                       'details',
                       'client',
                       'client_representation',
                       'contact_number',
                       'date_started',
                       'locality',
                       'contract_value',
                       'attachments')},
         ),
        audit_fieldset_tuple
    )


class ProjectsAdmin(ModelAdminMixin, admin.ModelAdmin):
    
    inlines = [
        CompletedProjectInline,
        OnGoingProjectInline]

    fieldsets = (
        (None, {
            'fields': ('cipa_id',)},
         ),
        audit_fieldset_tuple
    )

admin.site.register(Projects, ProjectsAdmin)

