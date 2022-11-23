from django.shortcuts import render,HttpResponseRedirect
from .forms import SingUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout 
# Create your views here.
def sing_up(request):
    if request.method == "POST":
        fm=SingUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=SingUpForm()
    return render (request, "app1/singup.html", {'fm':fm})

def login_up(request):
    if request.method == "POST":
        fm=AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data["username"]
            upass=fm.cleaned_data["password"]
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render (request,'app1/login.html',{'fm':fm})

def user_profile(request):
    return render (request,'app1/profile.html',{'name':request.user})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
