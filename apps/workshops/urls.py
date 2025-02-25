from django.urls import path
from . import views

app_name="workshops"
urlpatterns = [
    path('',views.ShowWorkshopList.as_view(), name='workshoplist'),
    path('workshopreport/<int:pk>',views.ShowWorkshopReport.as_view(), name='workshopreport'),
]
