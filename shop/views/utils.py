import random
from django.core.mail import send_mail
from django.conf import settings

def generate_verification_code():
    return str(random.randint(100000, 999999))

def send_verification_email(email):
    code = generate_verification_code()
    subject = "Email Verification Code"
    message = f"Your verification code is: {code}"
    from_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, from_email, [email], fail_silently=False)

    return code
