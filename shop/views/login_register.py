from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from shop.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from shop.forms import UserChangeForm
from django.contrib.auth.models import User


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'login-register/login-register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect('shop:home')
        return render(request, 'login-register/login-register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login-register/login-register.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:home')
        messages.error(request, "Invalid email or password!")
        return render(request, 'login-register/login-register.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('shop:home')


from django.contrib import messages




@login_required(login_url='login')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'profile/edit_profile.html', {'form': form})



def OTPView(request):
    return render(request, 'login-register/otp.html')