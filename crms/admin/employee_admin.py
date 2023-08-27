from django.contrib import admin
from ..models import (
    Employees, SeniorPermenantStaffBW,
    SeniorPermenantStaffForeigner)

class SeniorPermenantStaffBWInline(admin.TabularInline):
    model = SeniorPermenantStaffBW
    extra = 3


class SeniorPermenantStaffForeignerInline(admin.TabularInline):
    model = SeniorPermenantStaffForeigner
    extra = 3


class EmployeesAdmin(admin.ModelAdmin):
    
    inlines = [
        SeniorPermenantStaffBWInline,
        SeniorPermenantStaffForeignerInline]

admin.site.register(Employees, EmployeesAdmin)
