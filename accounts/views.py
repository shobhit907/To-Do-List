from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as logi,logout as logo
# Create your views here.
def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            logi(request,user)
            return redirect('homepage')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout(request):
    if request.method=='POST':
        logo(request)
        return redirect('homepage')