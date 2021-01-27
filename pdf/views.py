from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View,FormView, RedirectView
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import RegisterForm, LoginForm
from .models import RegisterModel


# Create your views here.


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/list'


class TmpView(TemplateView):
    template_name = 'index.html'


class LogView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/list'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        print(username, password, email)
        user = authenticate(username=email, password=password)
        user_ = RegisterModel.objects.get(username=username)
        if user is not None:
            if user_.is_block:
                print('this block')
                message = f"{user} is blocked by admin"
                return render(self.request,'login.html',{'msg': message,'form':form})
            else:
                login(self.request,user)
            print('username:-',user_.is_block)
        return super().form_valid(form)

class ShowView(LoginRequiredMixin,ListView):
    model = RegisterModel
    template_name = 'list.html'
    context_object_name = 'show'


class UserDetailView(DetailView):
    model = RegisterModel
    template_name = 'detail.html'
    context_object_name = 'detl'


class UserUpdateView(UpdateView):
    model = RegisterModel
    fields = ['username', 'profileImage', 'is_block']
    template_name = 'update.html'
    success_url = '/list'


class LogOutView(RedirectView):
    url = '/accounts/login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)