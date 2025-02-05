from django.core.mail import send_mail
from random import randint
from shop.models import VerificationCode

def generate_verification_code():
    return str(randint(100000, 999999))  # 6 raqamli OTP kodi

def send_verification_email(email, code):
    subject = "Tizimga Kirish uchun Kod"
    message = f"Sizning Tasdiqlash Kodingiz: {code}"
    from_email = 'akramibodullayev0011@gmail.com'  # O'zingizning email manzilingizni qo'yishingiz kerak
    send_mail(subject, message, from_email, [email])
    return code

def save_verification_code(email, code):
    verification_code, created = VerificationCode.objects.update_or_create(
        email=email, defaults={'code': code}
    )
    return verification_code
