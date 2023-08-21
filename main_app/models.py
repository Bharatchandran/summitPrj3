from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Interest(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('interest_list')


class Group(models.Model):
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('group_list', kwargs={'interest_id': self.id})


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
