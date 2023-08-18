from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Interest(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ForeignKey(User, on_delete=models.CASCADE)

class Topic(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)
    date = models.DateField()


