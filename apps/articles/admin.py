from django.contrib import admin
from .models import *

#------------------------------------------------------------------------------------
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','family','slug','email','is_active']
    list_filter=['family', 'slug']
    search_fields=('slug',)
    ordering = ('slug',)
    list_editable = ['is_active']

#------------------------------------------------------------------------------------
@admin.register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display = ['group_title']
    list_filter=['group_title']
    search_fields=('group_title',)
    ordering = ('group_title',)

#------------------------------------------------------------------------------------
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','register_date','slug','publish_date','is_active','view_number']
    list_filter=['title', 'slug']
    search_fields=('slug','key_words',)
    ordering = ('slug','title',)
    list_editable = ['is_active']

#------------------------------------------------------------------------------------
@admin.register(ArticleGallery)
class ArticleGalleryAdmin(admin.ModelAdmin):
    list_display = ['article','image_name']
    list_filter=['article']
    search_fields=('article',)
    ordering = ('article',)

#------------------------------------------------------------------------------------
