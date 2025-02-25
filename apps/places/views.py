from django.shortcuts import render, redirect
from . models import Place, TicketPrice, Message
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from .forms import MessageForm
from django.contrib import messages
#------------------------------------------------------------------------------------
def show_garden_history(request):
    return render(request, 'places_app/history.html')

#------------------------------------------------------------------------------------
def show_garden_parts(request):
    places=Place.objects.all()
    context={
       'places':places 
    }
    return render(request, 'places_app/parts.html', context)

#------------------------------------------------------------------------------------
def show_part_detail(request, id):
    place=Place.objects.get(id=id)
    return render(request, 'places_app/part_detail.html', {'place':place})

#------------------------------------------------------------------------------------
def download_path_garden(request):
    fs=FileSystemStorage()
    file_name="pdf_files/ferdowsGardenPath.pdf"
    if fs.exists(file_name):
        with fs.open(file_name) as pdf:
            response=HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition']="attachment; filename=ferdowsGardenPath.pdf"
            return response
    else:
        return HttpResponseNotFound("File Not Found...")
    
#------------------------------------------------------------------------------------
def show_time_rules(request):
    places=Place.objects.all()
    ticket_price=TicketPrice.objects.all().order_by('place')
    context={
        "ticket_price":ticket_price,
        "places":places
    }
    return render(request, "places_app/time_rules.html", context) 

#------------------------------------------------------------------------------------
def contact_view(request):
    form=MessageForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        msg=Message()
        msg.full_name=cd['full_name']
        msg.email=cd['email']
        msg.subject=cd['subject']
        msg.message=cd['message']
        msg.save()
        messages.add_message(request, 'پیام شما ارسال شد.', "success")
        return redirect('main:index')
    return render(request, 'places_app/contact.html', {'form':form})