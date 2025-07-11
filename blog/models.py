from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User      
from django.urls import reverse    #import the built in django model Users  

# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)              #update the date to latest date it was modified
    author=models.ForeignKey(User, on_delete= models.CASCADE)    #delete the post if the user is deleted

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
    
