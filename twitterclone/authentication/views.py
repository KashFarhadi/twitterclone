from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import TwitterUser
from .forms import SignupForm, LoginForm

from django.views import View
from django.views.generic.edit import FormView


class SignUpView(FormView):
    template_name = 'generic_form.html'
    form_class = SignupForm

    def get_context_data(self):
        context = super(SignUpView, self).get_context_data()
        context['title']='signup'
        return context

    def form_valid(self,form):
        data = form.cleaned_data
        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        login(self.request, user)
        TwitterUser.objects.create(
            name=data['username'],
            user=user
        )
        return HttpResponseRedirect(reverse('homepage'))


class LoginView(FormView):
    template_name = 'generic_form.html'
    form_class = LoginForm

    def get_context_data(self):
        context = super(LoginView, self).get_context_data()
        context['title']='Login to Twitterclone'
        return context
    
    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.request.GET.get('next','/'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('homepage'))
