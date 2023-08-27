from django.contrib import admin
from ..models import DirectorDetails, Directors

class DirectorDetailsInline(admin.TabularInline):
    model = DirectorDetails
    extra = 3

class DirectorsAdmin(admin.ModelAdmin):
    
    inlines = [DirectorDetailsInline]

admin.site.register(Directors, DirectorsAdmin)