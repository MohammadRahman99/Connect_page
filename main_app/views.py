from django.shortcuts import render,redirect
from .models import *
from .forms import ContactForm
# Create your views here.
def home(request):
    user_info=UserInfo.objects.all()
    context = {
        'user_info':user_info
        }
    return render(request,'index.html',context)

def contact(request):
    if request.method=='POST':
        form= ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    else:
        form = ContactForm()
    
    return render(request,'contact.html',{'form':form,'success':'Form submitted successfully'})

def projects(request):
    return render(request,'projects.html')

def resume(request):
    experience=Experience.objects.all()
    context = {
        'experience':experience
    }
    return render(request,'resume.html',context)