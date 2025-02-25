from django.contrib import admin
from .models import *

#------------------------------------------------------------------------------------
@admin.register(WorkshopStatus)
class WorkshopStatusAdmin(admin.ModelAdmin):
    list_display = ['status_code','status_title']

#------------------------------------------------------------------------------------
@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['title','place','view_number','register_date','is_active','status']
    list_filter=['place','status']
    search_fields=('title',)
    ordering = ('title','register_date',)
    list_editable = ['is_active']
    
#------------------------------------------------------------------------------------
@admin.register(WorkshopGallery)
class WorkshopGalleryAdmin(admin.ModelAdmin):
    list_display = ['workshop','image']
    list_filter=['workshop']
    search_fields=('workshop',)
    ordering = ('workshop',)

#------------------------------------------------------------------------------------