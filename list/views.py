from django.shortcuts import render,redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def showlist(request):
    items=Item.objects.all()
    return render(request,'list/list.html',{'items':items})

@login_required(login_url="accounts:login")
def additem(request):
    if request.method=='POST':
        form=forms.Additem(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('list:showlist')
    else:
        form=forms.Additem()
    return render(request,'list/items/additem.html',{'form':form})
