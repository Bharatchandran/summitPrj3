import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Interest, Topic, Group
from .forms import GroupForm, TopicForm, PostForm
from datetime import datetime
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class InterestList(LoginRequiredMixin, ListView):
    model = Interest


class InterestCreate(LoginRequiredMixin, CreateView):
    model = Interest
    fields = ['name']
    # form.owner = self.request.user

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class InterestUpdate(LoginRequiredMixin, UpdateView):
    model = Interest
    fields = ['name']


class InterestDelete(LoginRequiredMixin, DeleteView):
    model = Interest
    success_url = '/interests'


def group_list(request, interest_id):
    groups = Group.objects.filter(interest=interest_id)
    print(groups)
    return render(request, 'main_app/group_list.html', {
        'interest_id': interest_id,
        'groups': groups
    })


def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    topic_form = TopicForm()
    post_form = PostForm()
    # topic = Topic.objects.get()
    topics = group.topic_set.all()
    
    
   

    return render(request, 'main_app/group_detail.html', {
        'group': group,
        'topic_form': topic_form,
        'topics': topics,
        'post_form': post_form,
    })

# class GroupCreate(LoginRequiredMixin, CreateView):
#     model = Group
#     fields = ['name']
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


def group_new(request, interest_id):
    group_form = GroupForm()

    return render(request, 'main_app/group_new.html', {
        'group_form': group_form,
        'interest_id': interest_id
    })


def group_create(request, interest_id):
    form = GroupForm(request.POST)

    if form.is_valid():
        new_group = form.save(commit=False)
        new_group.interest_id = interest_id
        new_group.save()
    return redirect('group_list', interest_id=interest_id)


class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = ['name']


class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = '/interests'


def topic_create(request, group_id):
    form = TopicForm(request.POST)
    if form.is_valid():
        new_topic = form.save(commit=False)
        new_topic.group_id = group_id
        new_topic.save()
    return redirect('group_detail', group_id=group_id)


class TopicUpdate(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = ['name']


# class TopicDelete(LoginRequiredMixin, DeleteView):
#     model = Topic
#     # success_url = 'group_detail'
#     # success_url = '/interests'
#     group_id = model.group_id
#     success_url = reverse_lazy('group_detail', kwargs = {'group_id':group_id})

class TopicDelete(LoginRequiredMixin, DeleteView):
    model = Topic
    # success_url = 'group_detail'
    # success_url = '/interests'
    group_id = model.group_id

    def get_success_url(self):
        topic = self.get_object()
        group_id = topic.group_id
        success_url = reverse_lazy('group_detail', kwargs = {'group_id':group_id})
        return success_url

# def post_create(request,group_id, topic_id):
#     form = PostForm(request.POST)
#     if form.is_valid():
#         new_post = form.save(commit=False)
#         new_post.topic_id = topic_id
#         # new_post.user_id = request.user.id
#         new_post.save()
#     return redirect('group_detail',group_id=group_id)

def post_create(request,group_id, topic_id):
    form = PostForm(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.topic_id = topic_id
        # new_post.user_id = request.user.id
        photo_file = request.FILES.get('photo-file', None)
        if photo_file:
            s3 = boto3.client('s3')
            # need a unique "key" for S3 / needs image file extension too
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            # just in case something goes wrong
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                # build the full url string
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                # we can assign to cat_id or cat (if you have a cat object)
                new_post.image_url = url
            except Exception as e:
                print('An error occurred uploading file to S3')
                print(e)
        new_post.save()
    return redirect('group_detail',group_id=group_id)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['content']

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    def get_success_url(self):
        post = self.get_object()
        group_id = post.topic.group_id
        success_url = reverse_lazy('group_detail', kwargs = {'group_id':group_id})
        return success_url

# def add_photo(request, post_id):
#     # photo-file will be the "name" attribute on the <input type="file">
#     post = Post.objects.get(id = post_id)
#     group_id = post.topic.group_id
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         # need a unique "key" for S3 / needs image file extension too
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         # just in case something goes wrong
#         try:
#             bucket = os.environ['S3_BUCKET']
#             s3.upload_fileobj(photo_file, bucket, key)
#             # build the full url string
#             url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
#             # we can assign to cat_id or cat (if you have a cat object)
#             PostPhoto.objects.create(url=url, post_id=post_id)
#         except Exception as e:
#             print('An error occurred uploading file to S3')
#             print(e)
#     # return redirect('detail', group_id=group_id)
#     return 

def signup(request):
    error_message = ''
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('interest_list')
        else:
            error_message = 'Invalid sign up - try again'
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
