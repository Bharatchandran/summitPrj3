from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Interest, Topic, Group


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class InterestList(LoginRequiredMixin, ListView):
    model = Interest

class InterestDetail(LoginRequiredMixin, DetailView):
    model = Interest

class InterestCreate(LoginRequiredMixin, CreateView):
    model = Interest
    fields = ['name']

class InterestUpdate(LoginRequiredMixin, UpdateView):
    model = Interest
    fields = ['name']

class InterestDelete(LoginRequiredMixin, DeleteView):
    model = Interest
    success_url = '/interests'

class GroupList(LoginRequiredMixin, ListView):
    model = Group

class GroupDetail(LoginRequiredMixin, DetailView):
    model = Group

class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name']

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