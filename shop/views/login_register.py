from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from shop.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'login-register/login-register.html', {'register_form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(request, 'login-register/login-register.html', {'register_form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login-register/login-register.html', {'login_form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        messages.error(request, "Invalid email or password!")
        return render(request, 'login-register/login-register.html', {'login_form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
