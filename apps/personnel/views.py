from django.shortcuts import render
from .models import Personnel
from django.views.generic.list import ListView

#------------------------------------------------------------------------------------
class ShowPersonnelList(ListView):
    model = Personnel
    template_name = "personnel_app/personnel.html"
    context_object_name = "personnel"
    queryset = Personnel.objects.order_by('-is_active')