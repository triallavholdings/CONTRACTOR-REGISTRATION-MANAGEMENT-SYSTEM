from django.contrib import admin
from ..models import Shareholders, ShareholderDetails

class ShareholderDetailsInline(admin.TabularInline):
    model = ShareholderDetails
    extra = 3

class ShareholdersAdmin(admin.ModelAdmin):
    
    inlines = [ShareholderDetailsInline]

admin.site.register(Shareholders, ShareholdersAdmin)
