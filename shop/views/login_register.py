from django.views.generic import TemplateView


class LoginRegisterPageTemplateView(TemplateView):
    template_name = 'login-register/login-register.html'
