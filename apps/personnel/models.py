from django.db import models
from django.utils import timezone
from apps.gallery.models import FileUpload
#------------------------------------------------------------------------------------
class Personnel(models.Model):
    name=models.CharField(max_length=50,blank=True)
    family=models.CharField(max_length=50,blank=True)
    position=models.CharField(max_length=50,blank=True,verbose_name='سمت')
    mobile_number=models.CharField(max_length=11,unique=True,verbose_name='شماره موبایل')
    email=models.EmailField(max_length=200,blank=True)
    file_upload= FileUpload('images', 'personnel')
    image_name= models.ImageField(upload_to=file_upload.upload_to, verbose_name='تصویر پروفایل', null=True, blank=True)
    register_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ و زمان ثبت')
    is_active = models.BooleanField(default=False, verbose_name='وضعیت فعال/غیر فعال')
  
    
    def __str__(self):
        return self.name + " " + self.family
    
    class Meta:
        verbose_name_plural='کارکنان'
           
#------------------------------------------------------------------------------------