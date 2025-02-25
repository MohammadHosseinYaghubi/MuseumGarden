from django.urls import path
from . import views

app_name="articles"
urlpatterns = [
    path('',views.show_articles, name='blog'),
    path('<str:slug>/',views.show_blog_details, name='blog_details'),
    path('articlepdf/<int:article_id>/',views.show_article_pdf, name='article_pdf'),
    
]