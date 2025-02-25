from django.urls import path
from . import views

app_name="gallery"
urlpatterns = [
    path('galleries/',views.show_garden_galleries, name='galleries'),
    path('gallery_detail/<int:id>/',views.show_gallery_detail, name='gallery_detail'),
    
]