from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class PostIt(models.Model):
    author = models.ForeignKey(User, related_name='postit', on_delete=models.CASCADE)
    content = models.TextField('Content', null=False)
