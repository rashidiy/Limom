import random
import threading

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views import View

from shop.forms import RegistrationForm, UserChangeForm


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            password = user_data.pop('password1')
            user_data.pop('password2')
            if settings.DEBUG:
                verification_code = 123456
            else:
                verification_code = random.randint(100000, 999999)
                thread = threading.Thread(target=send_mail, args=(
                    'Email Verification',
                    f'Sizning tasdiqlash kodingiz: {verification_code}',
                    settings.EMAIL_HOST_USER,
                    [user_data['email']]))
                thread.start()
            request.session['pending_user'] = user_data
            request.session['pending_password'] = password
            request.session['verification_code'] = verification_code
            return redirect('shop:otp')
    else:
        form = RegistrationForm()

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


@login_required(login_url='shop:login')
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


def OPTView(request):
    if request.method == 'POST':
        input_code = request.POST.get('verification_code')
        stored_code = request.session.get('verification_code')
        pending_user = request.session.get('pending_user')
        pending_password = request.session.get('pending_password')

        if input_code and stored_code and str(input_code) == str(stored_code) and pending_user:
            user = User.objects.create_user(
                username=pending_user['username'],
                first_name=pending_user['first_name'],
                last_name=pending_user['last_name'],
                email=pending_user['email'],
                password=pending_password
            )
            user.is_active = True
            user.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            request.session.pop('pending_user', None)
            request.session.pop('pending_password', None)
            request.session.pop('verification_code', None)

            return redirect('shop:home')
        else:
            return render(request, 'login-register/otp.html', {
                'error': 'Invalid verification code'
            })

    return render(request, 'login-register/otp.html')


def forgot_password_view(request):
    step = 'email'

    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST.get('email')
            user = User.objects.filter(email=email).first()

            if user:
                otp_code = random.randint(100000, 999999)

                request.session['reset_email'] = email
                request.session['reset_otp'] = otp_code

                send_mail(
                    'Password Reset OTP',
                    f'Your OTP code: {otp_code}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

                step = 'otp'
            else:
                messages.error(request, 'This email is not registered.')

        elif 'otp_code' in request.POST:
            input_otp = request.POST.get('otp_code')
            stored_otp = request.session.get('reset_otp')

            if input_otp and str(input_otp) == str(stored_otp):
                step = 'reset_password'
            else:
                messages.error(request, 'Invalid OTP code')

        elif 'new_password' in request.POST:
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password == confirm_password:
                email = request.session.get('reset_email')
                user = User.objects.filter(email=email).first()

                if user:
                    user.set_password(new_password)
                    user.save()

                    request.session.pop('reset_otp', None)
                    request.session.pop('reset_email', None)

                    if user:
                        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request, 'Your password has been reset successfully!')
                    return redirect('shop:home')
                else:
                    messages.error(request, 'An error occurred. Try again.')
            else:
                messages.error(request, 'Passwords do not match.')
                step = 'reset_password'

    return render(request, 'login-register/forgot_password.html', {'step': step})
