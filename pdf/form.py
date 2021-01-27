from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import RegisterModel
from django import forms


class RegisterForm(UserCreationForm):

    class Meta():
        model = get_user_model()
        fields = ['username', 'email', 'profileImage', 'is_block']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    email = forms.CharField(label='email')







