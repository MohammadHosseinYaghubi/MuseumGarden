from django.contrib import admin
from .models import Personnel

#------------------------------------------------------------------------------------
@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('name','family','position','mobile_number','email','is_active')
    list_filter = ('is_active','position','family')
    list_editable = ['is_active',]
    
    fieldsets = (
        (None,{'fields':('mobile_number',)}),
        ('personal info',{'fields':('email','name','family','position','image_name',)}),
        ('status',{'fields':('is_active',)})
    )
    search_fields = ('position',)
