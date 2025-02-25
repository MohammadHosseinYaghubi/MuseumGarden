from django.urls import path
from . import views

app_name="personnel"
urlpatterns = [
    path('',views.ShowPersonnelList.as_view(), name='personnellist'),
    
]