from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .forms import LoginUserForm, UserCreationForm


class UserSignUpForm(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form = LoginUserForm
    template_name = 'users/login.html'


def logoutUser(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

