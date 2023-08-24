from django.contrib import admin
from .models import Interest, Group, Topic, Post, Like, Member


# Register your models here.
admin.site.register(Interest)
admin.site.register(Group)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Member)
