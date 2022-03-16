from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from .forms import RegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'user/home.html'

class RegisterUserView(CreateView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user:home')


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1200000)
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    pass


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user/users.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)