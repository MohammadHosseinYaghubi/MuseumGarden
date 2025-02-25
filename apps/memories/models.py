from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#------------------------------------------------------------------------------------
class Memory(models.Model):
    memory_title = models.CharField(max_length=200, verbose_name='عنوان خاطره')
    memory_text = models.TextField(verbose_name='متن خاطره')
    register_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ و زمان ثبت')
    is_active = models.BooleanField(default=False, verbose_name='وضعیت فعال/غیر فعال')
    user_registered = models.ForeignKey(User,on_delete=models.CASCADE, null=True, verbose_name='کاربر ثبت کننده')
    
    def __str__(self):
        return self.memory_title
    
    class Meta:
        verbose_name='خاطره'
        verbose_name_plural='خاطره ها'

#------------------------------------------------------------------------------------
def upload_gallery_image(instance,filename):
    return f"images/workshops/memory/{instance.memory.memory_title}/gallery/{filename}"

class MemoryGallery(models.Model):
    memory_image_name = models.ImageField(upload_to=upload_gallery_image, verbose_name='تصویر خاطره')
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, null=True, related_name='images')

#------------------------------------------------------------------------------------
class MemoryLike(models.Model):
    user_liked = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, null=True)
    
#------------------------------------------------------------------------------------