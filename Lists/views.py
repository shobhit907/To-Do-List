from django.shortcuts import render,redirect
from .models import Lists,Item
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse

# Create your views here.

@login_required(login_url="accounts:login")
def showLists(request):
    context={
        'lists':Lists.objects.filter(author=request.user)
    }
    return render(request,'Lists/showlists.html',context)

@login_required(login_url="accounts:login")
def createList(request):
    if request.method=='POST':
        form=forms.Lists(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('Lists:showLists')
    else:
        form=forms.Lists()
    return render(request,'Lists/createlist.html',{'form':form})

@login_required(login_url="accounts:login")
def displayList(request,slug):
    l=Lists.objects.filter(author=request.user,slug=slug)
    context={
        'list':Item.objects.filter(author=request.user ,lists=l[0]),
        'slugoflist':slug
    }
    return render(request,'Lists/displaylist.html',context)

@login_required(login_url="accounts:login")
def showItem(request,slug,slug1):
    l=Lists.objects.filter(author=request.user,slug=slug)
    context={
        'item':Item.objects.filter(author=request.user ,slug=slug1)[0],
    }
    return render(request,'Lists/showitem.html',context)
    

@login_required(login_url="accounts:login")
def addItem(request,slug):
    if request.method=='POST':
        form=forms.AddItem(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.lists=Lists.objects.filter(author=request.user,slug=slug)[0]
            instance.save()
            return displayList(request,slug)
    else:
        form=forms.AddItem()
    return render(request,'Lists/additem.html',{'form':form,'slugoflist':slug})
