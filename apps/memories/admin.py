from django.contrib import admin
from .models import *

#------------------------------------------------------------------------------------
@admin.register(Memory)
class TicketPriceAdmin(admin.ModelAdmin):
    list_display = ['memory_title', 'register_date', 'is_active', 'user_registered']
    list_editable = ['is_active']
