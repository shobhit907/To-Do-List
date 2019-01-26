from django.shortcuts import render,redirect
from .models import Lists
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
    context={
        'list':Lists.objects.filter(author=request.user, slug=slug)
    }
    return render(request,'Lists/displaylist.html',context)
    # return HttpResponse(slug)

