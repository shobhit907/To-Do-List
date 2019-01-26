from django import forms
from . import models

class Additem(forms.ModelForm):
    class Meta:
        model=models.Item
        fields=['title','description','todo_date','slug']
        