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
from .models import Post, Interest, Topic, Group, Like, Member
from .forms import GroupForm, TopicForm, PostForm
from datetime import datetime
from django.urls import reverse_lazy
from random import randrange
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class InterestList(LoginRequiredMixin, ListView):
    model = Interest
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = Group.objects.all()
        my_group = Member.objects.filter(user_id = self.request.user.id)
        # Add extra context data
        context['user_id'] = self.request.user.id
        context['groups'] = Group.objects.filter(owner_id = self.request.user.id)
        context['my_groups'] = my_group
        
        
        return context

class InterestCreate(LoginRequiredMixin, CreateView):
    model = Interest
    fields = ['name', 'description']
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
    interests = Interest.objects.all()
    currentInterest = Interest.objects.get(id=interest_id)
    user_id = request.user.id
    members = Member.objects.all().filter(user_id=user_id)
    # members = Group.objects.member_set.all().filter(user_id=user_id)
    print(members)
    return render(request, 'main_app/group_list.html', {
        'interest_id': interest_id,
        'groups': groups,
        'interests': interests,
        'currentInterest': currentInterest,
        'user_id': user_id,
        'members': members,
    })


def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    topic_form = TopicForm()
    post_form = PostForm()
    topics = group.topic_set.all()
    

    def user_like_post(self):
        print(self.user.id)
        return self.like_set.get(user_id = self.user.id)

    return render(request, 'main_app/group_detail.html', {
        'group': group,
        'topic_form': topic_form,
        'topics': topics,
        'post_form': post_form,
    })


def group_new(request, interest_id):
    group_form = GroupForm()

    return render(request, 'main_app/group_new.html', {
        'group_form': group_form,
        'interest_id': interest_id
    })


def group_create(request, interest_id):
    random_image = ["icon.svg","initials.svg","laurent.svg","laurent-round.svg","minidenticons.svg"]
    
    form = GroupForm(request.POST)

    if form.is_valid():
        new_group = form.save(commit=False)
        new_group.interest_id = interest_id
        new_group.owner = request.user
        photo_file = request.FILES.get('photo-file', None)
        if photo_file:
            s3 = boto3.client('s3')
            # need a unique "key" for S3 / needs image file extension too
            key = uuid.uuid4().hex[:6] + \
                photo_file.name[photo_file.name.rfind('.'):]
            # just in case something goes wrong
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                # build the full url string
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                # we can assign to cat_id or cat (if you have a cat object)
                new_group.image_url = url
            except Exception as e:
                print('An error occurred uploading file to S3')
                print(e)
        if not new_group.image_url:
            new_group.image_url = random_image[randrange(5)]


        new_group.save()
        
    return redirect('group_list', interest_id=interest_id)

    
def mygroup_index(request):
    member = Member.objects.all().filter(user_id=request.user.id)
    return render(request,'main_app/mygroup.html',{
        'member': member
    })
class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = ['name']


class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    # success_url = '/interests'
    def get_success_url(self):
        group = self.get_object()
        interest_id = group.interest_id
        success_url = reverse_lazy('group_list', kwargs={
                                   'interest_id': interest_id})
        return success_url


def topic_create(request, group_id):
    form = TopicForm(request.POST)
    if form.is_valid():
        new_topic = form.save(commit=False)
        new_topic.group_id = group_id
        new_topic.owner = request.user
        new_topic.save()
    return redirect('group_detail', group_id=group_id)


class TopicUpdate(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = ['name']


class TopicDelete(LoginRequiredMixin, DeleteView):
    model = Topic
    # success_url = 'group_detail'
    # success_url = '/interests'
    group_id = model.group_id

    def get_success_url(self):
        topic = self.get_object()
        group_id = topic.group_id
        success_url = reverse_lazy('group_detail', kwargs={
                                   'group_id': group_id})
        return success_url

# def topic_detail(request, topic_id):
#     group = Group.objects.get()
#     topic = Topic.objects.get(id=topic_id)
#     topic_form = TopicForm()
#     post_form = PostForm()
#     topics = group.topic_set.all()

#     def user_like_post(self):
#         print(self.user.id)
#         return self.like_set.get(user_id = self.user.id)

#     return render(request, 'main_app/topic_detail.html', {
#         'group': group,
#         'topic_form': topic_form,
#         'topics': topics,
#         'post_form': post_form,
#         'topic': topic,
#     })

def topic_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic_form = TopicForm()
    post_form = PostForm()
    group = topic.group
    
    def user_like_post(self):
        print(self.user.id)
        return self.like_set.get(user_id = self.user.id)

    return render(request, 'main_app/topic_detail.html', {
        'group': group,
        'topic_form': topic_form,
        'post_form': post_form,
        'topic': topic,
    })

def post_create(request, group_id, topic_id):
    form = PostForm(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.topic_id = topic_id
        new_post.user_id = request.user.id
        # new_post.user_id = request.user.id
        photo_file = request.FILES.get('photo-file', None)
        if photo_file:
            s3 = boto3.client('s3')
            # need a unique "key" for S3 / needs image file extension too
            key = uuid.uuid4().hex[:6] + \
                photo_file.name[photo_file.name.rfind('.'):]
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
    return redirect('topic_detail', topic_id)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['content']


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        post = self.get_object()
        group_id = post.topic.group_id
        success_url = reverse_lazy('group_detail', kwargs={
                                   'group_id': group_id})
        return success_url


def add_member_to_group(request,interest_id,group_id):
    Member.objects.create(user_id=request.user.id, group_id=group_id, interest_id=interest_id)
    return redirect('group_detail', group_id=group_id)

def create_like(request, group_id, post_id):
    post = Post.objects.get(id=post_id)
    like = post.like_set.filter(user=request.user)
    print(like)
    if len(like) == 0:
        Like.objects.create(post_id=post_id, user_id= request.user.id )
    return redirect('group_detail', group_id=group_id)


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