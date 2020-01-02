from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import TwitterUser
from .forms import SignupForm, LoginForm

from django.views import View
from django.views.generic.edit import FormView


def signup_view(request):
    html = 'generic_form.html'
    form = None

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'], 
                password=data['password']
            )
            login(request, user)
            TwitterUser.objects.create(
                name=data['username'],
                user=user
            )
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return(request, '<h1>form not valid</h1>')

    else:
        form = SignupForm()
    return render(request, html, {'form':form, 'title': 'Sign Up Now!'})


def login_view(request):
    html='generic_form.html'
    form = None
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next','/'))
    else:
        form = LoginForm()
    return render(request, html, {'form':form, 'title': 'Login to Django-Twitterclone'})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))