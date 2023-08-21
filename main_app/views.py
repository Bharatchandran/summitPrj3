from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Interest, Topic, Group
from .forms import GroupForm

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
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class InterestUpdate(LoginRequiredMixin, UpdateView):
    model = Interest
    fields = ['name']

class InterestDelete(LoginRequiredMixin, DeleteView):
    model = Interest
    success_url = '/interests'

# class GroupList(LoginRequiredMixin, ListView):
#     model = Group
def group_list(request, interest_id):
    groups = Group.objects.filter(interest=interest_id)
    print(groups)
    return render(request, 'main_app/group_list.html',{
        'groups':groups,
        'interest_id': interest_id
    })

class GroupDetail(LoginRequiredMixin, DetailView):
    model = Group

def group_detail(request, interest_id):
    pass

# class GroupCreate(LoginRequiredMixin, CreateView):
#     model = Group
#     fields = ['name']
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

def group_new(request, interest_id):
    group_form = GroupForm()
    
    return render(request, 'main_app/group_new.html',{
        'group_form': group_form,
        'interest_id':interest_id
        })

def group_create(request, interest_id):
    form = GroupForm(request.POST)

    if form.is_valid():

        new_group = form.save(commit=False)
        new_group.interest_id = interest_id
        new_group.member_id = interest_id

        new_group.save()
    return redirect('group_list', interest_id= interest_id)

class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = ['name']

class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = '/groups'

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