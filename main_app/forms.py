from django.forms import ModelForm
from .models import Group, Topic


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
