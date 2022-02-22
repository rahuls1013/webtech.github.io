from django.shortcuts import render
from .models import contact
# Create your views here.
def home(request):
    return render(request,'user/index.html')


def about(request):
    return render(request,'user/about.html')


def news(request):
    return render(request,'user/signin.html')

def video(request):
    return render(request,'user/guider.html')

def contactus(request):
    status=False
    if request.method=='POST':
        a=request.POST.get("name","")
        b=request.POST.get("email","")
        c=request.POST.get("mobile","")
        d=request.POST.get("msg","")
        x=contact(name=a,email=b,mobile=c,message=d)
        x.save()
        status=True
    return render(request,'user/contactus.html',{'S':status})








