from django.contrib import admin
from .models import Gallery, MuseumGallery

#------------------------------------------------------------------------------------
#=========================================
class MuseumGalleryInline(admin.TabularInline):
    model = MuseumGallery
    extra = 1
#=========================================
@admin.register(Gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display = ('title_text', 'place_id', 'gallery_parent', 'slug',)
    search_fields = ('image_name',)
    ordering = ('title_text','image_name',)
    inlines = [MuseumGalleryInline]

    fieldsets = (
        ('اطلاعات تصویر',{'fields':(
                        'image_name','place_id',
                        ('title_text',),
                        'gallery_parent',
                        'slug'
                        )}),
    )