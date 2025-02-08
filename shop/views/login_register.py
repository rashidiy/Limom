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


class SignupView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'login-register/login-register.html', {'form': form})

    def post(self, request):
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


class EditProfileView(View):
    def get(self, request):
        form = UserChangeForm(instance=request.user)
        return render(request, 'profile/edit_profile.html', {'form': form})

    def post(self, request):
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
        return render(request, 'profile/edit_profile.html', {'form': form})




class OTPView(View):
    def get(self, request):
        return render(request, 'login-register/otp.html')

    def post(self, request):
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
        return render(request, 'login-register/otp.html', {'error': 'Invalid verification code'})


import random
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views import View

class ForgotPasswordView(View):
    def get(self, request):
        request.session['step'] = 'email'
        return render(request, 'login-register/forgot_password.html', {'step': 'email'})

    def post(self, request):
        step = request.session.get('step', 'email')

        # 1-qadam: Emailni tekshirish va OTP yuborish
        if step == 'email':
            email = request.POST.get('email')
            user = User.objects.filter(email=email).first()

            if user:
                otp_code = random.randint(100000, 999999)
                request.session['reset_email'] = email
                request.session['reset_otp'] = str(otp_code)
                request.session['step'] = 'otp'

                # OTP yuborish
                send_mail(
                    'Password Reset OTP',
                    f'Your OTP code: {otp_code}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

                return render(request, 'login-register/forgot_password.html', {'step': 'otp'})

            messages.error(request, 'This email is not registered.')

        # 2-qadam: OTP tekshirish
        elif step == 'otp':
            input_otp = request.POST.get('otp_code')
            stored_otp = request.session.get('reset_otp')

            if input_otp and stored_otp and input_otp == stored_otp:
                request.session['step'] = 'reset_password'
                return render(request, 'login-register/forgot_password.html', {'step': 'reset_password'})

            messages.error(request, 'Invalid OTP code')

        # 3-qadam: Parolni yangilash
        elif step == 'reset_password':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password == confirm_password:
                email = request.session.get('reset_email')

                if not email:
                    messages.error(request, 'Session expired! Please try again.')
                    return redirect('shop:forgot_password')

                user = User.objects.filter(email=email).first()
                if user:
                    user.set_password(new_password)
                    user.save()

                    # Sessiyalarni tozalash
                    request.session.pop('reset_otp', None)
                    request.session.pop('reset_email', None)
                    request.session.pop('step', None)

                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request, 'Your password has been reset successfully!')
                    return redirect('shop:home')

                messages.error(request, 'An error occurred. Try again.')
            else:
                messages.error(request, 'Passwords do not match.')

        return render(request, 'login-register/forgot_password.html', {'step': request.session.get('step', 'email')})



