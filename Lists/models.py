from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Lists(models.Model):
    name=models.CharField(max_length=400)
    slug=models.SlugField(blank=False)
    author=models.ForeignKey(User,default=None,on_delete=True)
    
    def __str__(self):
        return self.name
