from django import forms
from . import models

class Lists(forms.ModelForm):
    class Meta:
        model=models.Lists
        fields=['name']
