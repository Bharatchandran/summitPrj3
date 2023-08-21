from django.forms import ModelForm
from .models import Group, Topic, Post


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['name']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']