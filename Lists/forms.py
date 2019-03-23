from django import forms
from . import models
from django.contrib.auth.models import User

class Lists(forms.ModelForm):
    class Meta:
        model=models.Lists
        fields=['name','slug']

class AddItem(forms.ModelForm):
    class Meta:
        model=models.Item
        fields=['title','description','todo_date','slug']

class AddUser(forms.Form):
    username=forms.CharField(label='Enter username of the user you want to add',max_length=100)

