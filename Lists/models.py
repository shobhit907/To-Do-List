from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Lists(models.Model):
    name=models.CharField(max_length=400)
    slug=models.SlugField(blank=False)
    author=models.ManyToManyField(User,default=None)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    todo_date=models.DateTimeField(blank=True,null=True)
    slug=models.SlugField()
    author=models.ManyToManyField(User,default=None)
    lists=models.ForeignKey(Lists,on_delete=models.CASCADE,blank=False,default=None)
    
    def __str__(self):
        return self.title


