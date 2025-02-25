from django.db import models
from django.utils import timezone

#------------------------------------------------------------------------------------
class Place(models.Model):
    place_name=models.CharField(max_length=100, verbose_name='نام مکان')
    information=models.TextField(verbose_name='توضیحات', default='توضیحات')
    place_image_name=models.ImageField(upload_to="images/places/", verbose_name='تصویر')
    visiting_day=models.CharField(max_length=100, verbose_name='روزهای بازدید')
    visiting_hour=models.CharField(max_length=100, verbose_name='ساعت بازدید')
    rules=models.TextField(verbose_name='قوانین و مقررات')
    register_date=models.DateTimeField(default=timezone.now, verbose_name='تاریخ و زمان ثبت')
    
    def __str__(self):
        return self.place_name
    
    class Meta:
        verbose_name='مکان'
        verbose_name_plural='مکانها'
        db_table='t_Places'

#------------------------------------------------------------------------------------
class VisitorType(models.Model):
    type_name=models.CharField(max_length=100, verbose_name='نام نوع بازدید کننده')
    
    def __str__(self):
        return self.type_name
    
    class Meta:
        verbose_name='نوع بازدید کننده'
        verbose_name_plural='نوع بازدید کننده ها' 
        db_table='t_visitor_type'
        
#------------------------------------------------------------------------------------
class TicketPrice(models.Model):
    place=models.ForeignKey(Place,on_delete=models.CASCADE, verbose_name='مکان مورد نظر')
    visitor_type=models.ForeignKey(VisitorType,on_delete=models.CASCADE, verbose_name='نوع بازدید کننده')
    price=models.IntegerField(default=0, verbose_name='بهای بلیط')
    
    def __str__(self):
        return f"{self.place}\t{self.visitor_type}\t{self.price}"
    
    class Meta:
        verbose_name='قیمت'
        verbose_name_plural='قیمت ها'
        db_table='t_ticket_prices'

#------------------------------------------------------------------------------------
class Message(models.Model):
    full_name=models.CharField(max_length=60, verbose_name='نام و نام خانوادگی')
    email=models.EmailField(max_length=250, verbose_name='ایمیل')
    subject=models.CharField(max_length=200, verbose_name='عنوان پیام')
    message=models.TextField(verbose_name='متن پیام')
    is_seen=models.BooleanField(default=False, verbose_name='وضعیت مشاهده توسط مدیر')
    register_date=models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت پیام')
    
    def __str__(self):
        return f"{self.full_name}\t{self.subject}\t{self.register_date}"
    
    class Meta:
        verbose_name='پیام'
        verbose_name_plural='پیام ها'
        db_table='t_messages'

#------------------------------------------------------------------------------------
