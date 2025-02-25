from django.db import models
import os
from uuid import uuid4
from django.utils import timezone
#------------------------------------------------------------------------------------
class FileUpload:
    def __init__(self,dir,prefix):
        self.dir=dir
        self.prefix=prefix
    def upload_to(self,instance,filename):
        filename, ext=os.path.splitext(filename)
        return f'{self.dir}/{self.prefix}/{uuid4()}{ext}'

#------------------------------------------------------------------------------------
class Gallery(models.Model):
    place_id=models.IntegerField(verbose_name='کد مکان')
    title_text=models.CharField(max_length=200, verbose_name='متن عنوان',null=True, blank=True)
    file_upload=FileUpload('images','gallery')
    image_name=models.ImageField(upload_to=file_upload.upload_to, verbose_name='تصویر اصلی')
    register_date=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درج')
    gallery_parent = models.ForeignKey('Gallery', on_delete=models.CASCADE, blank=True, null=True, related_name="galleries_child", verbose_name='والد تصویر')
    slug=models.SlugField(max_length=200, null=True)
    
    def __str__(self):
        return f"{self.title_text}"
    
    class Meta:
        verbose_name='تصویر'
        verbose_name_plural='تصاویر'
        db_table='t_gallery'

#------------------------------------------------------------------------------------
class MuseumGallery(models.Model):
    gallery=models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='تصویر', related_name='gallery_images')
    file_upload=FileUpload('images','museum_gallery')
    image_name=models.ImageField(upload_to=file_upload.upload_to, verbose_name='تصویر مرتبط')
    title=models.CharField(max_length=200, verbose_name='عنوان',null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name='تصویر'
        verbose_name_plural='تصاویر'
        db_table='t_museum_gallery'