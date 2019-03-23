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
    l=Lists.objects.get(author=request.user,slug=slug)
    context={
        'list':Item.objects.filter(author=request.user ,lists=l),
        'slugoflist':slug,
        'listname':l.name,
    }
    return render(request,'Lists/displaylist.html',context)

@login_required(login_url="accounts:login")
def showItem(request,slug,slug1):
    try:
        l=Lists.objects.get(author=request.user,slug=slug)
        a=Item.objects.get(author=request.user ,slug=slug1,lists=l)
    except:
        a=None
    context={
        'item':a,
        'slugoflist':slug
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


@login_required(login_url="accounts:login")
def deleteItem(request,slug,slug1):
    try:
        l=Lists.objects.get(author=request.user,slug=slug)
        Item.objects.get(author=request.user,slug=slug1,lists=l).delete()
        # item.delete()
        return redirect("Lists:displayList",slug=slug)
    except:
        return HttpResponse("Error")