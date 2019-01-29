from django import forms
from . import models

class Lists(forms.ModelForm):
    class Meta:
        model=models.Lists
        fields=['name','slug']

class AddItem(forms.ModelForm):
    class Meta:
        model=models.Item
        fields=['title','description','todo_date','slug']