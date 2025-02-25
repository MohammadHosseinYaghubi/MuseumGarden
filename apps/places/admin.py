from django.contrib import admin
from .models import Place,VisitorType,TicketPrice,Message

#------------------------------------------------------------------------------------ 
@admin.register(Place)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['place_name', 'place_image_name', 'visiting_day', 'visiting_hour', 'register_date']
    list_filter=['place_name']
    search_fields=('place_name',)
    ordering = ('place_name',)

#------------------------------------------------------------------------------------
@admin.register(VisitorType)
class VisitorTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']
    list_filter=['type_name']
    search_fields=('type_name',)
    ordering = ('type_name',)

#------------------------------------------------------------------------------------
@admin.register(TicketPrice)
class TicketPriceAdmin(admin.ModelAdmin):
    list_display = ['place', 'visitor_type', 'price']
    list_filter=['place', 'price']
    search_fields=('place',)
    ordering = ('place',)
    list_editable = ['price']

#------------------------------------------------------------------------------------
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'email', 'is_seen', 'register_date']
    list_filter=['subject', 'is_seen', 'register_date']
    search_fields=('subject',)
    ordering = ('subject',)
    list_editable = ['is_seen']