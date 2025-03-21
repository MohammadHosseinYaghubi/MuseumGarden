# Generated by Django 5.0.4 on 2024-04-10 01:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=250, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=200, verbose_name='عنوان پیام')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('is_seen', models.BooleanField(default=False, verbose_name='وضعیت مشاهده توسط مدیر')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ثبت پیام')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
                'db_table': 't_messages',
            },
        ),
    ]
