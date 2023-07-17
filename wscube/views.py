from django.http import HttpResponse
from django.shortcuts import render,redirect
from skill.models import skill
from contactsave.models import contact_save
from django.core.mail import send_mail
from django.contrib import messages

def aboutus(request):
    return HttpResponse("<b>welocme to my websites</b>")

def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=contact_save(name=name,email=email,subject=subject,message=message)
        data.save()
        messages.success(request,"I'll Contact You Soon")
        return redirect('home')
    


def home(request):
    skilldata=skill.objects.all()
    data={'skilldata':skilldata}
    return render(request,"index.html",data)
    
    
def course(request):
    return render(request,"index.html")

def coursedetail(request,courseid):
    return HttpResponse(courseid) 


    
      



        
        
          


