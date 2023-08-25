from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from datetime import date
import datetime

# Create your models here.
class Interest(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    createdAt = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-createdAt']
    def __str__(self):
        return f"{self.name}:{self.id}"

    def get_absolute_url(self):
        return reverse('interest_list')


class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    # member = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-createdAt']
    def __str__(self):
        return f"{self.name}:{self.id}"
    def get_absolute_url(self):
        group = Group.objects.get(id=self.id)
        return reverse('group_list', kwargs={'interest_id': group.interest_id})


class Topic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField('Topic', max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']
    
    def __str__(self):
        return f"{self.name}:{self.id}"
    
    def get_absolute_url(self):
        print(self,"-------")
        topic = Topic.objects.get(id=self.id)
        group = topic.group_id
        return reverse('group_detail', kwargs={'group_id':group})


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    image_url = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']

    def get_absolute_url(self):
        post = Post.objects.get(id=self.id)
        group = post.topic.group_id
        return reverse('group_detail', kwargs={'group_id': group})


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    group= models.ForeignKey(Group, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)