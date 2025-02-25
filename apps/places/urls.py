from django.urls import path
from . import views

app_name="places"
urlpatterns = [
    path('history/',views.show_garden_history, name='history'),
    path('parts/',views.show_garden_parts, name='parts'),
    path('part_detail/<int:id>/',views.show_part_detail, name='part_detail'),
    path('pdf_path/',views.download_path_garden, name='pdf_path'),
    path('time_rules/',views.show_time_rules, name='time_rules'),
    path('contact/',views.contact_view, name='contact'),
    
]
