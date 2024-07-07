from django.shortcuts import render
from .models import UserInfo
# Create your views here.
def home(request):
    user_info=UserInfo.objects.all()
    context = {
        'user_info':user_info
        }
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'projects.html')

def resume(request):
    return render(request,'resume.html')