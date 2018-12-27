from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete='None')
    title=models.CharField(max_length=50)
    content=models.TextField(default=' ')
    image=models.ImageField(upload_to='media/post_img/')
    created=models.DateTimeField(default=datetime.datetime.now())
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.title
