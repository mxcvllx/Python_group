from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from account.forms import CustomAuthenticationForm, UserRegistrationForm


class AccountLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "account/login.html"


def custom_login(request):
    form = CustomAuthenticationForm(request.POST or None)
    if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is not None and password:
            user = authenticate(
                request, username=username, password=password
            )
            login(request, user)
            return redirect("account:profile")
    return render(request, "account/login.html", {"form": form})


@login_required
def profile(request):
    return render(request, "account/profile.html", {"user": request.user})


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("account:login")
