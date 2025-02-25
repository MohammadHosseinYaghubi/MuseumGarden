from django.shortcuts import render, get_object_or_404,redirect
from .models import Gallery,MuseumGallery
import os

#------------------------------------------------------------------------------------
def show_garden_galleries(request):
    galleries=Gallery.objects.all()
    context={
       'galleries':galleries
    }
    return render(request, 'gallery_app/gallery.html', context)

#------------------------------------------------------------------------------------
def show_gallery_detail(request, id):
    gallery=get_object_or_404(Gallery, id=id)
    return render(request, 'gallery_app/gallery_detail.html', {'gallery':gallery})