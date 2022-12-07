from django.urls import path
from django.contrib.auth.views import LogoutView

from main.settings import LOGOUT_REDIRECT_URL
from .views import UserSignUpForm, LoginUser, logout


urlpatterns = [
    path('logout/', LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL), name='logout'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', UserSignUpForm.as_view(), name='register'),
]