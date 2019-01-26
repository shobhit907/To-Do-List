from django.db import models
from django.contrib.auth.models import User
from Lists.models import Lists
# Create your models here.

class Item(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    todo_date=models.DateTimeField(blank=True,null=True)
    slug=models.SlugField()
    author=models.ForeignKey(User,default=None,on_delete=True)
    lists=models.ForeignKey(Lists,on_delete=models.CASCADE,blank=False,default=None)
    
    def fillslug(self):
        title=str(self.title)
        for c in title:
            if (c>='a' and c<='z') or (c>='A' and c<='Z') or (c>='0' and c<='9') :
                self.slug+=c
            else:
                self.slug+='-'

    def __str__(self):
        return self.title